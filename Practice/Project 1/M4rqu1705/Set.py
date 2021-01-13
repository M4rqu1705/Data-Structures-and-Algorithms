#!/usr/bin/env python
# -*- coding: utf-8 -*-

using_primes = True

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


DEFAULT_SIZE = 10

class Set:
    '''
    This Python script implements a set using hashes.

    It does it's best for the average time complexity to be O(1) to O(n) for most of the operations

    For the worst case scenarios (where there are hash collisions), the time complexity for those
    operations increases to O(n) to O(n²)

    '''
    def __init__(self, param = None):
        self.current_size = 0
        self.primes_generator = primes()

        # By default the method will simply make an empty set with the default capacity
        if param is None:
            self.array_list = [None] * DEFAULT_SIZE

        # If param is an integer, we can use it as the initial set capacity
        elif isinstance(param, int):
            self.array_list = [None] * param

        # Finally, if param is anything else, assume it is an iterator and try to populate the set
        # with its data
        else:
            self.array_list = [None] * DEFAULT_SIZE
            try:
                iter(param)
                for element in param:
                    self.add(element)

            # If the iterator assumption is false, then just ignore everything
            except:
                pass


    # Time complexity: O(n)
    def expand(self):
        if using_primes:
            new_capacity = next(self.primes_generator)
            while (new_capacity <= self.capacity()):
                new_capacity = next(self.primes_generator)
        else:
            new_capacity = self.capacity() * 2

        tempSet = Set(new_capacity)

        # Add every element from this set to the new set
        for el in self:
            tempSet.add(el)

        # Reassign array_list to be the new Set's set
        self.array_list = tempSet.array_list[:]


    # Time complexity: O(n)
    def contract(self):
        # Make new set half the size of this set
        tempSet = Set(self.capacity() // 2)

        # Add every element from this set to the new set
        for el in self:
            tempSet.add(el)

        # Reassign array_list to be the new Set's set
        self.array_list = tempSet.array_list[:]


    # Average-case time complexity: O(1)
    # Worst-case time complexity: O(n)
    def contains(self, element):
        # Make hash and divide it modulo the set's length in order to find it's position
        position = hash(element) % self.capacity()

        # If the element was sucessfully found:
        if self.array_list[position] == element:
            return True

        # Otherwise
        else:
            print("Colission!")
            # Perform linear search to look for the element
            return element in self.array_list


    # Average-case time complexity: O(1)
    # Worst-case time complexity: O(n)
    def add(self, element):
        # Elements cannot be repeated
        if element in self:
            return False

        if using_primes:
            if self.size() + 1 > self.capacity() * 0.7:
                self.expand()
        else:
            if self.size() + 1 > self.capacity() * 0.5:
                self.expand()


        # Make hash and divide it modulo the set's ggth in order to find it's position
        position = hash(element) % self.capacity()

        # If the element was not found:
        if self.array_list[position] is None:
            self.array_list[position] = element
            self.current_size += 1
            return True

        # Otherwise ...
        else:
            # Perform linear search until empty slot is found
            for i in range(self.capacity()):
                if self.array_list[i] is None:
                    self.array_list[i] = element
                    self.current_size += 1
                    return True


    # Average-case time complexity: O(1)
    # Worst-case time complexity: O(n)
    def remove(self, element):
        # Element must be inside the set in order to be removed
        if element not in self:
            return False

        # Contract set whenever it's length is close to getting to a quarter of it's capacity
        if self.size() < self.capacity() // 4:
            self.contract()

        # Make hash and divide it modulo the set's length in order to find it's position
        position = hash(element) % self.capacity()

        # If the element was found:
        if self.array_list[position] == element:
            self.array_list[position] = None
            self.current_size -= 1
            return True

        # Otherwise ...
        else:
            # Perform linear search until element is found
            for i in range(self.capacity()):
                if self.array_list[i] == element:
                    self.array_list[i] = None
                    self.current_size -= 1
                    return True

            return False


    # Time complexity: O(n)
    def clear(self):
        # Store capacity of previous set
        capacity = self.capacity()

        # Delete set
        del self.array_list

        # Create new one with the previous capacity, but none of the elements
        self.array_list = [None] * capacity
        self.current_size = 0

        return True


    # Equivalent to the length (or the amount of actual elements it has)
    # Time complexity: O(1)
    def size(self):
        return self.current_size


    # Equivalent to how many elements it would be able to hold
    # Time complexity: O(1)
    def capacity(self):
        return len(self.array_list)


    # Equivalent to the size / capacity ratio
    # Time complexity: O(1)
    def load_factor(self):
        return self.size() / self.capacity()


    # Time complexity: O(1)
    def isEmpty(self):
        return self.size() == 0


    # Average-case time complexity: O(n)
    # Worst-case time complexity: O(n²)
    def union(self, s2):
        s3 = Set()

        # Add all of self's and s2's elements to s3
        for el in self:
            s3.add(el)

        for el in s2:
            s3.add(el)

        return s3


    # Average-case time complexity: O(min(n, m))
    # Worst-case time complexity: O(n * m)
    def intersection(self, s2):
        s3 = Set()

        # Determine which is the smallest set
        small_set = None
        big_set = None

        if self.size() < s2.size():
            small_set = self
            big_set = s2
        else:
            small_set = s2
            big_set = self

        # Use the smallest set to iterate the least amount of times through the sets
        for el in small_set:
            if el in big_set:
                s3.add(el)

        return s3

    # Average-case time complexity: O(n)
    # Worst-case time complexity: O(n²)
    def difference(self, s2):
        s3 = Set()

        # Add every element from self to s3 ...
        for el in self:
            s3.add(el)

        # but then remove any common elements between s3 and s2
        for el in s2:
            if el in s3:
                s3.remove(el)

        return s3


    # Average-case time complexity: O(n)
    # Worst-case time complexity: O(n²)
    def subset(self, s2):
        for el in s2:
            if el not in self:
                return False

        return True


    # 🎆🎇🎉🎊 MAGIC METHODS 🧝‍♂️🧙‍♂️🧙‍♀️

    # String representation of this set
    def __str__(self):
        return str(list(self))

    # Get the current size of this set
    def __len__(self):
        return self.current_size

    # Machine readable representation of this set
    def __repr__(self):
        return str(list(self))

    # When testing membership with the "in" operator
    def __contains__(self, el):
        return self.contains(el)

    # When this set is added with another, return union
    def __add__(self, s2):
        return self.union(s2)

    # When this set is multiplied with another, return intersection
    def __mul__(self, s2):
        return self.intersection(s2)

    # When this set is the minuend, return difference with other set
    def __sub__(self, s2):
        return self.difference(s2)

    # When this set is the subtrahend, return difference with other set
    def __rsub__(self, s1):
        return s1.difference(self)

    # When this set is less than or equal to other set, return subset function
    def __le__(self, s1):
        return s1.subset(self)

    # When this set is greater than or equal to other set, return subset function
    def __ge__(self, s2):
        return self.subset(s2)

    # When this set is less than another set, return subset function and if the other set is greater than this one
    def __lt__(self, s1):
        return s1.subset(self) and len(s1) > len(self)

    # When this set is greater than another set, return subset function and if this set is greater than other set
    def __gt__(self, s2):
        return self.subset(s2) and len(self) > len(s2)

    # When sets are equal, their difference will be 0
    def __eq__(self, s2):
        return (self - s2).size() == 0

    # When sets are not equal, it is the opposite of when they are equal
    def __ne__(self, s2):
        return not(self == s2)

    # When using bool() method
    def __bool__(self):
        return not self.isEmpty()

    def __hash__(self) -> int:
        '''Generate a hash of this Set using `FNV1A hash
        <https://en.wikipedia.org/wiki/Fowler%E2%80%93Noll%E2%80%93Vo_hash_function>`_

        Makes a copy of this Set and uses FNV1A hash with a little tweak (I
        use modulo 1E19 just so numbers don't get TOO big)

        Returns:
            int: This Set's hash code

        Hint:
            Time complexity: O(n)
        
        '''
        total = 2166136261

        for element in self:
            total *= 16777619
            total ^= hash(element)
            # A little extra just to prevent numbers from getting tooo big
            total % int(1E19)

        return total


    # Iterator methods
    def __iter__(self):
        self.iterationIndex = 0
        return self

    def __next__(self):
        while self.iterationIndex < self.capacity():
            self.iterationIndex += 1
            if self.array_list[self.iterationIndex - 1] is None:
                continue
            else:
                return self.array_list[self.iterationIndex - 1]

        raise StopIteration


if __name__ == "__main__":
    set1 = Set()
    for i in range(65,159):
        # Using ascii characters
        set1.add(chr(i))
        # Using only the numbers
        set1.add(i)
        # Using a sequence of consecutive ascii characters
        set1.add(str(chr(i) + chr(i+1)))

    #  set2 = Set()
    #  for i in range(65,91):
        #  set2.add(chr(i))

    #  set3 = Set()
    #  for i in range(65,70):
        #  set3.add(chr(i))

    #  set4 = Set()
    #  for i in range(70,91):
        #  set4.add(chr(i))

    print('---')
    for el in set1:
        set1.contains(el)

    breakpoint()
