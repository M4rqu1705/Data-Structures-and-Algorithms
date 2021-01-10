#!/usr/bin/env python
# -*- coding: utf-8 -*-
from typing import Any, NoReturn

DEFAULT_SIZE = 10
class Bag:
    '''Multiset Data Structure

    | Unordered collection of elements where repetitions are allowed.
    |
    | Implemented as an Array List that gets expanded as needed

    Attributes:
       current_size(int): Stores how many elements are in the bag
       array_list(list): ArrayList Data Structure that contains the data from bag

    '''

    def __init__(self, param: Any = None) -> NoReturn:
        '''Bag constructor

        Args:
           any: integer, Bag or iterator that is used to populate the bag's array list

        Raises:
           TypeError: Occurs when param is not an integer, iterator nor other Bag

        Example:
           >>> bag1 = Bag()
           >>> bag1
           []
           >>> bag2 = Bag([1,2,3])
           >>> bag2
           [1,2,3]
           >>> bag3 = Bag(bag2)
           >>> bag3
           [1,2,3]

        '''

        self.current_size = 0

        if isinstance(param, int):
            self.array_list = [None] * param
        elif isinstance(param, Bag):
            self.array_list = [None] * param.capacity()

            for element in param:
                self.add(element)
        else:
            try:
                iter(param)

                self.array_list = [None] * (len(param) + 1)

                for element in param:
                    self.add(element)

            except TypeError:
                self.array_list = [None] * DEFAULT_SIZE

            except:
                raise TypeError("invalid literal `param` for Bag constructor. Not an integer, iterator nor other Bag") from None


    def expand(self) -> NoReturn:
        '''Expand array list capacity with which the Bag is implemented

        Duplicates the capacity of the array list by making a new Bag, adding all this
        bag's elements to the new Bag and, copying the new bag's array list to this
        one

        Hint:
           Time complexity: O(n)

        '''
        # Make new Bag twice the size of this bag
        temp_bag = Bag( int(self.capacity() * 2) )

        # Add every element from temp_bag to the new bag
        for el in self:
            temp_bag.add(el)

        # Reassign array_list to be the temp_bag's bag
        self.array_list = temp_bag.array_list[:]


    def contract(self) -> NoReturn:
        '''Contract array list capacity with which the Bag is implemented

        Halves the capacity of the array list by making a new Bag, adding all this
        bag's elements to the new Bag and, copying the new bag's array list to this
        one

        Hint:
           Time complexity: O(n)

        '''
        # Make new Bag half the size of this bag
        temp_bag = Bag( int(self.capacity() // 2) )

        # Add every element from temp_bag to the new bag
        for el in self:
            temp_bag.add(el)

        # Reassign array_list to be the temp_bag's bag
        self.array_list = temp_bag.array_list[:]


    def contains(self, element: Any) -> bool:
        '''Test for element membership
        
        Checks if the passed element is inside this bag. Implemented with Linear Search

        Args:
           any: Element that is looked for in bag

        Returns:
           bool: True if element is inside bag

        Example:
           >>> bag = Bag([1,2,3])
           >>> bag.contains(2)
           True
           >>> bag.contains(100)
           False

        Hint:
           Time complexity: O(n)

        '''

        # Perform linear search to look for the element
        return element in self.array_list


    def add(self, element: Any) -> NoReturn:
        '''Adds new element

        Before adding element, expand array list if necessary

        Args:
           any: The element to be added to Bag

        Returns:
           bool: True if operation was successful

        Example:
           >>> bag = Bag()
           >>> bag
           []
           >>> bag.add(0)
           True
           >>> bag
           [0]
           >>> bag.add(3)
           True
           >>> bag
           [0, 3]
           >>> bag.add(10)
           True
           >>> bag
           [0, 3, 10]

        Hint:
           | Average Time complexity: O(1)
           | Worst-case Time complexity: O(n)

        '''
        # Expand bag whenever it's length after the append is greater than the capacity
        if self.size() + 1 > self.capacity():
            self.expand()

        # Add new element at last available position
        self.array_list[self.current_size] = element
        self.current_size += 1
        return True


    def remove(self, element: Any) -> bool:
        '''Remove a copy of an element

        It will specifically remove the first copy

        Args:
           any: The element to be removed from the bag

        Returns:
           bool: True if operation was successful

        Example:
           >>> bag = Bag([1,5,3])
           >>> bag
           [1, 5, 3]
           >>> bag.remove(1)
           True
           >>> bag
           [3, 5]

        Hint:
           Time complexity: O(n)

        '''

        # Contract bag whenever it's length is close to getting to half of it's capacity
        if self.size() < self.capacity() // 2:
            self.contract()

        i = 0

        # Perform linear search from back to front until element is found
        while self.array_list[i] is not None:
            if self.array_list[i] == element:

                # Substitute element to be removed with last element of bag
                self.array_list[i] = self.array_list[self.current_size - 1]
                # Substitute last element of bag with None
                self.array_list[self.current_size - 1] = None
                self.current_size -= 1

                return True

            i += 1

        return False


    def remove_all(self, element: Any) -> int:
        '''Remove all copies of an element

        Args:
           any: The value of the elements to be removed from the bag

        Returns:
           int: Amount of elements removed from Bag

        Example:
           >>> bag = Bag([1,2,2,3,2,5,6,6])
           >>> bag.remove_all(2)
           3
           >>> bag.remove_all(6)
           6
           >>> bag
           [1, 3, 5]

        Hint:
           Time complexity: O(n)

        '''

        # Contract bag whenever it's length is close to getting to half of it's capacity
        if self.size() < self.capacity() // 2:
            self.contract()

        counter = 0
        i = 0

        # Perform linear search while removing elements
        while self.array_list[i] is not None:
            if self.array_list[i] == element:

                # Substitute element to be removed with last element of bag
                self.array_list[i] = self.array_list[self.current_size - 1]
                # Substitute last element of bag with None
                self.array_list[self.current_size - 1] = None

                self.current_size -= 1
                counter += 1

            i += 1

        return counter


    def clear(self) -> NoReturn:
        '''Clear bag
        
        Simply delete the array_list followed by making a new array_list with
        the same capacity as before filled with "None"

        Example:
           >>> bag = Bag([1,2,3,4,3])
           >>> bag
           [1, 2, 3, 4, 3]
           >>> bag.clear()
           True
           >>> bag
           []

        Hint:
            Time complexity: O(n)

        '''
        # Store capacity of previous bag
        capacity = self.capacity()

        # Delete bag
        del self.array_list

        # Create new one with the previous capacity, but none of the elements
        self.array_list = [None] * capacity
        self.current_size = 0

        return True


    def count(self, element: Any) -> int:
        '''Count copies of element

        Perform Linear Search and add to counter when element is found

        Args:
           any: Value whose count will be found

        Returns:
           int: Amount of times element was found

        Example:
           >>> bag = Bag([1,2,3,2,2])
           >>> bag.count(2)
           3

        Hint:
           Time complexity: O(n)
        
        '''

        counter = 0
        # Perform linear search for element
        for i in range(self.size()):
            if self.array_list[i] == element:
                counter += 1

        return counter


    def size(self) -> int:
        '''Get bag size

        Returns the actual amount of elements Bag has

        Returns:
           int: length of bag

        Hint:
           Time complexity: O(1)
        
        '''
        return self.current_size


    def capacity(self) -> int:
        '''Get bag size

        Returns the maximum amount of elements this bag's array list can hold

        Returns:
           int: Capacity of bag

        Hint:
           Time complexity: O(1)
        
        '''
        return len(self.array_list)


    def isEmpty(self) -> bool:
        '''Test if empty

        Returns:
           bool: True if bag is empty

        Hint:
           Time complexity: O(1)

        '''
        return self.size() == 0


    def __str__(self) -> str:
        '''String representation of this bag

        Simply iterates through bag and appends elements to list. Then converts
        list to string

        Returns:
           str: String representation of bag

        Hint:
           Time complexity: O(n)
        
        '''
        return str(list(self))

    def __repr__(self) -> str:
        '''Machine-readable representation of this bag

        Simply calls bag's :py:meth:`Bag.Bag.__str__` method

        Returns:
           str: Machine-readable representation of bag

        Hint:
           Time complexity: O(n)
        
        '''
        return str(self)

    def __len__(self) -> int:
        '''Simply calls this bag's size method

        See :py:meth:`Bag.Bag.size` for more details

        Returns:
           int: Length of bag

        Hint:
           Time complexity: O(1)

        '''
        return self.size()

    # When testing membership with the "in" operator
    def __contains__(self, el) -> bool:
        '''Simply calls this bag's contains method

        See :py:meth:`Bag.Bag.contains` for more details

        Returns:
           bool: True if element is inside bag

        Hint:
           Time complexity: O(n)
        
        '''
        return self.contains(el)

    def __add__(self, b2: Any) -> Any:
        '''Merge bag and iterator

        When this bag is added with an iterator, merge both into bag. Otherwise,
        simply add element to bag

        Args:
           any: Iterator to merge with bag or element to add to it

        Returns:
           Bag: Bag after merging iterator or element added

        Hint:
           Time complexity: O(n + m)

        '''
        try:
            temp_bag = Bag(self.size() + len(b2))
            iter(b2)


            for el in self:
                temp_bag.add(el)

            for el in b2:
                temp_bag.add(el)

            return temp_bag

        except TypeError:
            temp_bag = Bag(self.size() + 1)

            for el in self:
                temp_bag.add(el)

            temp_bag.add(b2)

            return temp_bag

    def __bool__(self) -> bool:
        '''Simply calls this bag's isEmpty method and negates it

        See :py:meth:`Bag.Bag.isEmpty` for more information

        Returns:
           bool: True if bag is NOT empty

        Hint:
           Time complexity: O(1)

        '''
        return not self.isEmpty()

    def __hash__(self) -> int:
        '''Generate a hash of this Bag using `FNV1A hash
        <https://en.wikipedia.org/wiki/Fowler%E2%80%93Noll%E2%80%93Vo_hash_function>`_

        Makes a copy of this Bag and uses FNV1A hash with a little tweak (I
        use modulo 1E19 just so numbers don't get TOO big)

        Returns:
            int: This Bag's hash code

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
    def __iter__(self) -> Any:
        self.iterationIndex = 0
        return self

    def __next__(self) -> Any:
        if self.iterationIndex < self.size() and self.array_list[self.iterationIndex] is not None:
            self.iterationIndex += 1
            return self.array_list[self.iterationIndex-1]
        else:
            raise StopIteration



if __name__ == "__main__":
    bag1 = Bag()
    for i in range(66,90):
        bag1.add(chr(i))
        bag1.add(chr(i+1))
        bag1.add(chr(i-1))

    breakpoint()
