#!/usr/bin/env python
# -*- coding: utf-8 -*-
from typing import Any, NoReturn

class Map:
    class Node:
        def __init__(self):
            self.key = None
            self.value = None
            self.next = None

    
    def __init__(self):
        self.head = self.Node()
        self.current_size = 0


    def put(self, key: Any, value: Any) -> bool:
        '''Add new value to the map with a given key

        Args:
           any: Key to the value that will be added
           any: Value to be added to the map

        Returns:
           bool: Operation was successful

        Hint:
           Time complexity: O(n)
        '''

        if value is None:
            return False

        if self.containsKey(key):
            self.remove(key)

        new_node = self.Node()
        new_node.key = key
        new_node.value = value
        new_node.next = self.head.next
        self.head.next = new_node

        self.current_size += 1

        return True


    def remove(self, key: Any) -> bool:
        '''Remove value with given key from map

        Args:
           any: Key to the value that will be removed

        Returns:
           bool: Operation was successful

        Hint:
           Time complexity: O(n)
        '''

        if not self.containsKey():
            return False

        current_node = self.head

        while current_node.next.key != key and current_node.next.next is not None:
            current_node = current_node.next

        temp = current_node.next
        current_node.next = current_node.next.next
        del temp

        self.current_size -= 1

        return True


    def get(self, key: Any) -> Any:
        '''Get value associated with key

        Args:
           any: Key of the value being searched for

        Returns:
           any: None if not found, value if it was found

        Hint:
           Time complexity: O(n)
        '''

        if self.isEmpty():
            return None

        current_node = self.head

        while current_node.next.key != key and current_node.next.next is not None:
            current_node = current_node.next

        if current_node.next.key != key:
            return None
        else:
            return current_node.next.value


    def containsKey(self, key: Any) -> bool:
        '''Determines if there is a value with a given key

        Args:
           any: Key that will be looked for inside map

        Returns:
           bool: True if key is contained inside map

        Hint:
           Time complexity: O(n)
        '''

        return self.get(key) is not None


    def getKeys(self) -> Any:
        '''Generator of all the keys in map

        Returns:
           Any: Latest key in map

        Hint:
           Time complexity: O(n)
        '''

        for key, value in self:
            yield key


    def getValues(self) -> Any:
        '''Generator of all the values in map

        Returns:
           Any: Latest value in map

        Hint:
           Time complexity: O(n)
        '''

        for key, value in self:
            yield value


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


    def clear(self) -> NoReturn:
        '''Clear map

        Remove all values in map, effectively returning it to its initial
        condition

        Hint:
           Time complexity: O(n)

        '''

        while self.head.next is not None:
            temp = self.head.next
            self.head.next = self.head.next.next
            del temp

        self.current_size = 0

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
        '''Represent map in string format as sequence of key, value tuples

        Returns:
           str: String representation of map

        Hint:
           Time complexity: O(n)

        '''
        message = []

        for key, value in self:
            message.append(''.join(["(", str(key), ", ", str(value), ")"]))

        return ', '.join(message)


    def __repr__(self) -> str:
        '''Represent map in machine-readable string format as sequence of key, value tuples

        Returns:
           str: Machine-readable string representation of map

        Hint:
           Time complexity: O(n)

        '''
        return str(self)


    def __iter__(self) -> Any:
        self.iteration_node = self.head.next
        return self

    def __next__(self):
        if self.iteration_node is not None:
            key, value = self.iteration_node.key, self.iteration_node.value
            self.iteration_node = self.iteration_node.next
            return (key, value)
        else:
            raise StopIteration





if __name__ == "__main__":
    m = Map()
    m.put("Sue", 14)
    m.put("Tom", 12)
    m.put("John", 10)
    m.put("Isabella", 10)
    m.put("John", 8)

    breakpoint()

