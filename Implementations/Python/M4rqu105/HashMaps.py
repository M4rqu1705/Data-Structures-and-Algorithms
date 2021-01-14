#!/usr/bin/env python
# -*- coding: utf-8 -*-
from typing import Any, NoReturn

DEFAULT_SiZE = 10

# Customized primes generator comprehension
def primes():
    yield 1
    yield 2
    yield 3
    yield 5
    yield 7
    i = 9
    while True:
        isPrime = True

        # Simple sqrt approximation (https://en.wikipedia.org/wiki/Methods_of_computing_square_roots#Bakhshali_method)
        end = ((i*i + 24*i + 16)/(8*i + 32))
        end = int(end) + 1

        for j in range(3, end):
            if i % j == 0:
                isPrime = False
                break

        if isPrime:
            yield i
        i += 2


class SeparateChaining:
    __slots__ = ['buckets', 'current_size', 'primes_generator', 'keys_generator']

    class BucketNode:
        __slots__ = ['key', 'value', 'next']

        def __init__(self):
            self.key = None
            self.value = None
            self.next = None

        def __str__(self) -> str:
            return f'"{str(self.key)}": {str(self.value)}'

        def __repr__(self) -> str:
            return str(self)


    def __init__(self, param: Any = None):
        self.current_size = 0
        self.primes_generator = primes()

        if param is None:
            self.buckets = [self.BucketNode() for i in range(DEFAULT_SiZE)]

        elif isinstance(param, int):
            self.buckets = [self.BucketNode() for i in range(param)]

        elif isinstance(param, SeparateChaining):
            self = param.copy()

        else:
            raise TypeError(f"Expected int or SeparateChaining object, not {type(param)}")


    def expand(self) -> NoReturn:
        new_capacity = next(self.primes_generator)
        while (new_capacity // 2 < self.amount_buckets()):
            new_capacity = next(self.primes_generator)

        tempSC = SeparateChaining(new_capacity)

        for key, value in self.items():
            tempSC.put(key, value)

        self.current_size = tempSC.size()
        self.buckets = tempSC.buckets[:]


    def put(self, key: Any, value: Any) -> bool:
        '''Add new value to the map with a given key

        Args:
           any: Key to the value that will be added
           any: Value to be added to the map

        Returns:
           bool: Operation was successful

        Hint:
           Time complexity: O(1 + n/N)
        '''

        try:
            hash(key)
        except:
            #  raise TypeError(f"Key of type {type(key)} is not hashable")
            return False

        if self.load_factor() >= 1.0:
            self.expand()

        position = hash(key) % self.amount_buckets()

        # Remove element from hash table if it is already in it
        self.remove(key)


        newNode = self.BucketNode()
        newNode.key = key
        newNode.value = value
        newNode.next = self.buckets[position].next

        self.buckets[position].next = newNode

        self.current_size += 1

        return True


    def remove(self, key: Any) -> bool:
        '''Remove value with given key from map

        Args:
           any: Key to the value that will be removed

        Returns:
           bool: Operation was successful

        Hint:
           Time complexity: O(1 + n/N)
        '''

        try:
            hash(key)
        except:
            #  raise TypeError(f"Key of type {type(key)} is not hashable")
            return False

        if not self.containsKey(key):
            return False

        position = hash(key) % self.amount_buckets()

        bucket = self.buckets[position]

        while bucket.next is not None and bucket.next.key != key:
            bucket = bucket.next

        if bucket.next is None:
            return False
    

        temp = bucket.next
        bucket.next = bucket.next.next
        del temp

        self.current_size -= 1


    def get(self, key: Any) -> Any:
        '''Get value associated with key

        Args:
           any: Key of the value being searched for

        Returns:
           any: None if not found, value if it was found

        Hint:
           Time complexity: O(1 + n/N)
        '''

        if self.isEmpty():
            return None

        position = hash(key) % self.amount_buckets()

        bucket = self.buckets[position]

        while bucket.next is not None and bucket.next.key != key:
            bucket = bucket.next

        if bucket.next is None:
            return None
        else:
            return bucket.next.value


    def containsKey(self, key: Any) -> bool:
        '''Determines if there is a value with a given key

        Args:
           any: Key that will be looked for inside map

        Returns:
           bool: True if key is contained inside map

        Hint:
           Time complexity: O(1 + n/N)
        '''

        return self.get(key) is not None


    def getKeys(self) -> Any:
        '''Generator of all the keys in map

        Returns:
           Any: Latest key in map

        Hint:
           Time complexity: O(n)
        '''

        for bucket in self.buckets:
            while bucket.next is not None:
                bucket = bucket.next
                yield bucket.key
    

    def getValues(self) -> Any:
        '''Generator of all the values in map

        Returns:
           Any: Latest value in map

        Hint:
           Time complexity: O(n)
        '''

        for bucket in self.buckets:
            while bucket.next is not None:
                bucket = bucket.next
                yield bucket.value


    def size(self) -> int:
        '''Get number of values in map

        Returns:
           int: Amount of values stored in map

        Hint:
           Time complexity: O(1)
        '''
        return self.current_size


    def isEmpty(self) -> bool:
        '''Test if map is empty

        Returns:
           bool: True if the size of the map is 0

        Hint:
           Time complexity: O(1)
        '''
        return self.size() == 0 


    def amount_buckets(self) -> int:
        '''Get number of buckets in map
        
        Returns:
           int: Amount of buckets available in map

        Hint:
           Time complexity: O(1)
        '''
        return len(self.buckets)


    def load_factor(self) -> float:
        '''Get load factor of map
        
        Returns:
           float: Size divided by amount of buckets

        Hint:
           Time complexity: O(1)
        '''
        return self.size() / self.amount_buckets()

    
    def clear(self) -> NoReturn:
        '''Clear map

        Remove all values in map, effectively returning it to its initial
        condition

        Hint:
           Time complexity: O(n)

        '''

        for i in range(self.amount_buckets()):
            while self.buckets[i].next is not None:
                temp = self.buckets[i].next
                self.buckets[i].next = self.buckets[i].next.next
                del temp

    
    def copy(self):
        newMap = SeparateChaining(self.capacity())

        for key, value in self.items():
            newMap.put(key, value)

        return newMap


    def items(self):
        '''Generator to help iterate through map's key-value pairs

        Returns:
           tuple: Tuple of a key-value pair

        Hint:
           Time complexity: O(n)

        '''
        temp = zip(self.getKeys(), self.getValues())
        for el in temp:
            yield el


    def __contains__(self, param: Any) -> bool:
        '''By default, when using the `in` Python operator, check if the
        parameter is a key of this map

        Returns:
           bool: True if key is contained inside map

        Hint:
           Time complexity: O(1 + n/N)
        '''

        return self.containsKey(param)


    def __str__(self) -> str:
        '''Represent map in string format as a Python dictionary

        Returns:
           str: String representation of map

        Hint:
           Time complexity: O(n)

        '''
        message = []
        temp = []

        for i in range(self.amount_buckets()):
            bucket = self.buckets[i]

            while bucket.next is not None:
                temp.append(str(bucket.next))
                bucket = bucket.next

            message.extend(temp)
            temp = []

        return ', '.join(message)


    def __repr__(self) -> str:
        '''Represent map in machine-readable string format as Python dictionary

        Returns:
           str: Machine-readable string representation of map

        Hint:
           Time complexity: O(n)

        '''
        return f"{{{str(self)}}}"


    def __iter__(self):
        self.keys_generator = self.getKeys()
        return self
    def __next__(self):
        key = next(self.keys_generator)
        return key


# ⚠ NOT WORKING ⚠
class OpenAddressing:
    __slots__ = ['buckets', 'current_size', 'primes_generator', 'keys_generator']

    class BN:
        __slots__ = ['key', 'value', 'inUse']

        def __init__(self):
            self.key = None
            self.value = None
            self.inUse = False

        def __str__(self) -> str:
            return f'"{str(self.key)}": {str(self.value)}'

        def __repr__(self) -> str:
            return str(self)


    def __init__(self, param: Any = None):
        self.current_size = 0
        self.primes_generator = primes()

        if param is None:
            self.buckets = [self.BN() for i in range(DEFAULT_SiZE)]

        elif isinstance(param, int):
            self.buckets = [self.BN() for i in range(param)]

        elif isinstance(param, OpenAddressing):
            self = param.copy()

        else:
            raise TypeError(f"Expected int or OpenAddressing object, not {type(param)}")


    def expand(self) -> NoReturn:
        new_capacity = next(self.primes_generator)
        while (new_capacity // 2 < self.capacity()):
            new_capacity = next(self.primes_generator)

        tempSC = OpenAddressing(new_capacity)

        for key, value in self.items():
            tempSC.put(key, value)

        self.current_size = tempSC.size()
        self.buckets = tempSC.buckets[:]


    def put(self, key: Any, value: Any) -> bool:
        '''Add new value to the map with a given key

        Args:
           any: Key to the value that will be added
           any: Value to be added to the map

        Returns:
           bool: Operation was successful

        Hint:
           | Average time complexity: O(1)
           | Worst-case time complexity: O(n)
        '''

        try:
            hash(key)
        except:
            #  raise TypeError(f"Key of type {type(key)} is not hashable")
            return False

        if self.load_factor() >= 0.4:
            self.expand()

        position = hash(key) % self.capacity()

        # Remove element from hash table if it is already in it
        self.remove(key)

        # if the bucket at the specified position is in use ...
        if self.buckets[position].inUse:
            # Cuadratically probe for next available slot
            i = 1
            while not self.buckets[(position + i) % self.capacity()].inUse and i < self.capacity():
                i += 1

            self.buckets[(position + i) % self.capacity()].key = key
            self.buckets[(position + i) % self.capacity()].value = value
            self.buckets[(position + i) % self.capacity()].inUse = True

        else:
            self.buckets[position].key = key
            self.buckets[position].value = value
            self.buckets[position].inUse = True


        self.current_size += 1

        return True


    def remove(self, key: Any) -> bool:
        '''Remove value with given key from map

        Args:
           any: Key to the value that will be removed

        Returns:
           bool: Operation was successful

        Hint:
           | Average time complexity: O(1)
           | Worst-case time complexity: O(n)
        '''

        try:
            hash(key)
        except:
            #  raise TypeError(f"Key of type {type(key)} is not hashable")
            return False

        if not self.containsKey(key):
            return False

        position = hash(key) % self.capacity()

        # if the bucket at the specified position is not the one we're looking for
        if not (self.buckets[position].inUse and self.buckets[position].key == key):
            # Cuadratically probe for bucket with correct key
            i = 1
            while not (self.buckets[(position + i) % self.capacity()].inUse and self.buckets[(position + i) % self.capacity()].key == key) and i < self.capacity():
                i += 1

            # Mark bucket as not in use
            self.buckets[(position + i) % self.capacity()].key = None
            self.buckets[(position + i) % self.capacity()].value = None
            self.buckets[(position + i) % self.capacity()].inUse = False

        else:
            # Mark bucket as not in use
            self.buckets[position].key = None
            self.buckets[position].value = None
            self.buckets[position].inUse = False

        self.current_size -= 1

        return True


    def get(self, key: Any) -> Any:
        '''Get value associated with key

        Args:
           any: Key of the value being searched for

        Returns:
           any: None if not found, value if it was found

        Hint:
           | Average time complexity: O(1)
           | Worst-case time complexity: O(n)
        '''

        if self.isEmpty():
            return None

        position = hash(key) % self.capacity()

        try:
            self.buckets[position].inUse
        except:
            breakpoint()
        if not (self.buckets[position].inUse and self.buckets[position].key == key):
            # Cuadratically probe for bucket with correct key
            i = 1
            while not (self.buckets[(position + i) % self.capacity()].inUse and self.buckets[(position + i) % self.capacity()].key == key) and i < self.capacity():
                i += 1

            # From this point on, probing results with exactly the same values
            if i < self.capacity():
                return self.buckets[(position + i) % self.capacity()].value
            else:
                # if after probing element was not found, return None
                return None

        else:
            return self.buckets[position].value

    def containsKey(self, key: Any) -> bool:
        '''Determines if there is a value with a given key

        Args:
           any: Key that will be looked for inside map

        Returns:
           bool: True if key is contained inside map

        Hint:
           | Average time complexity: O(1)
           | Worst-case time complexity: O(n)
        '''

        return self.get(key) is not None


    def getKeys(self) -> Any:
        '''Generator of all the keys in map

        Returns:
           Any: Latest key in map

        Hint:
           Time complexity: O(n)
        '''

        for bucket in self.buckets:
            if bucket.inUse:
                yield bucket.key
    

    def getValues(self) -> Any:
        '''Generator of all the values in map

        Returns:
           Any: Latest value in map

        Hint:
           Time complexity: O(n)
        '''

        for bucket in self.buckets:
            if bucket.inUse:
                yield bucket.value


    def size(self) -> int:
        '''Get number of values in map

        Returns:
           int: Amount of values stored in map

        Hint:
           Time complexity: O(1)
        '''
        return self.current_size


    def isEmpty(self) -> bool:
        '''Test if map is empty

        Returns:
           bool: True if the size of the map is 0

        Hint:
           Time complexity: O(1)
        '''
        return self.size() == 0 


    def capacity(self) -> int:
        '''Get number of buckets in map
        
        Returns:
           int: Amount of buckets available in map

        Hint:
           Time complexity: O(1)
        '''
        return len(self.buckets)


    def load_factor(self) -> float:
        '''Get load factor of map
        
        Returns:
           float: Size divided by amount of buckets

        Hint:
           Time complexity: O(1)
        '''
        return self.size() / self.capacity()

    
    def clear(self) -> NoReturn:
        '''Clear map

        Remove all values in map, effectively returning it to its initial
        condition

        Hint:
           Time complexity: O(n)

        '''

        for i in range(self.capacity()):
            self.buckets[i].key = None
            self.buckets[i].value = None
            self.buckets[i].inUse = False

    
    def copy(self):
        newMap = OpenAddressing(self.capacity())

        for key, value in self.items():
            newMap.put(key, value)

        return newMap


    def items(self):
        '''Generator to help iterate through map's key-value pairs

        Returns:
           tuple: Tuple of a key-value pair

        Hint:
           Time complexity: O(n)

        '''
        temp = zip(self.getKeys(), self.getValues())
        for el in temp:
            print(el)
            yield el


    def __contains__(self, param: Any) -> bool:
        '''By default, when using the `in` Python operator, check if the
        parameter is a key of this map

        Returns:
           bool: True if key is contained inside map

        Hint:
           | Average time complexity: O(1)
           | Worst-case time complexity: O(n)
        '''

        return self.containsKey(param)


    def __str__(self) -> str:
        '''Represent map in string format as a Python dictionary

        Returns:
           str: String representation of map

        Hint:
           Time complexity: O(n)

        '''
        message = []

        for i in range(self.capacity()):
            if self.buckets[i].inUse:
                message.append(str(self.buckets[i]))

        return ', '.join(message)


    def __repr__(self) -> str:
        '''Represent map in machine-readable string format as Python dictionary

        Returns:
           str: Machine-readable string representation of map

        Hint:
           Time complexity: O(n)

        '''
        return f"{{{str(self)}}}"


    def __iter__(self):
        self.keys_generator = self.getKeys()
        return self
    def __next__(self):
        key = next(self.keys_generator)
        return key


if __name__ == "__main__":
    #  sc = SeparateChaining()
    #  sc.put("Daniel", 40)
    #  sc.put("Zakira", 38)
    #  sc.put("Francisco", 44)
    #  sc.put("Darlene", 41)
    #  sc.put("Sofía", 15)
    #  sc.put("Marcos", 19)
    #  sc.put("Taimí", 11)
    #  sc.put("Maribel", 6)
    #  sc.put("Nandy", 66)
    #  sc.put("Awi", 70)
    #  sc.put("Débora", 19)
    #  sc.put("Daniela", 21)

    #  print(sc)

    oa = OpenAddressing()
    oa.put("Daniel", 40)
    oa.put("Francisco", 44)
    oa.put("Darlene", 41)
    oa.put("Sofía", 15)
    oa.put("Marcos", 19)
    oa.put("Taimí", 11)
    oa.put("Maribel", 6)
    oa.put("Nandy", 66)
    oa.put("Awi", 70)
    oa.put("Débora", 19)
    oa.put("Daniela", 21)
    oa.put("Zakira", 38)
    
    print(oa)
    print(oa.size())

    breakpoint()
