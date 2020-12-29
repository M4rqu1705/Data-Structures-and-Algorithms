#!/usr/bin/env python
# -*- coding: utf-8 -*-
DEFAULT_SIZE = 10

class Bag:
    def __init__(self, dataType, initial_capacity = DEFAULT_SIZE):
        self.currentSize = 0
        self.myBag = [None] * initial_capacity
        self.dataType = dataType


    # 🔧🔨⛏ HELPER FUNCTIONS ⚙🛠⚒

    # Time complexity: O(1)
    def validElement(self, element):
        # Check if bag has correct data type
        if not isinstance(element, self.dataType):
            # If it is not, try to force it
            try:
                element = self.dataType(element)
                return True
            # If it cannot be forced, then element cannot be in bag
            except:
                return False
        else:
            return True


    # Time complexity: O(n)
    def expand(self):
        # Make new bag twice the size of this bag
        tempBag = Bag(self.dataType, self.capacity() * 2)

        # Add every element from this bag to the new bag
        for el in self:
            tempBag.add(el)

        # Reassign myBag to be the new Bag's bag
        self.myBag = tempBag.myBag[:]


    # Time complexity: O(n)
    def contract(self):
        # Make new bag twice the size of this bag
        tempBag = Bag(self.dataType, self.capacity() // 2)

        # Add every element from this bag to the new bag
        for el in self:
            tempBag.add(el)

        # Reassign myBag to be the new Bag's bag
        self.myBag = tempBag.myBag[:]



    # 👜🎒 BAG ADT METHODS 💼🏎

    # Time complexity: O(n)
    def contains(self, element):
        # Force element to be desired data type if it is valid
        if not self.validElement(element):
            return False
        else:
            element = self.dataType(element)

        # Perform linear search to look for the element
        return element in self.myBag


    # Average-case time complexity: O(1)
    # Worst-case time complexity: O(n)
    def add(self, element):
        # Force element to be desired data type if it is valid
        if not self.validElement(element):
            return False
        else:
            element = self.dataType(element)

        # Expand bag whenever it's length after the append is greater than the capacity
        if self.size() + 1 > self.capacity():
            self.expand()

        # Add new element at last available position
        self.myBag[self.currentSize] = element
        self.currentSize += 1
        return True


    # Time complexity: O(n)
    def remove(self, element):
        # Force element to be desired data type if it is valid
        if not self.validElement(element):
            return False
        else:
            element = self.dataType(element)

        # Contract bag whenever it's length is close to getting to half of it's capacity
        if self.size() < self.capacity() // 2:
            self.contract()

        # Perform linear search from back to front until element is found
        for i in range(self.size() - 1, -1, -1):
            if self.myBag[i] == element:

                # Substitute element to be removed with last element of bag
                self.myBag[i] = self.myBag[self.currentSize - 1]
                # Substitute last element of bag with None
                self.myBag[self.currentSize - 1] = None
                self.currentSize -= 1

                return True

            # Exit early whenever the first None is found
            elif self.myBag[i] is None:
                break

        return False


    # Time complexity: O(n)
    def remove_all(self, element):
        # Force element to be desired data type if it is valid
        if not self.validElement(element):
            return False
        else:
            element = self.dataType(element)

        # Contract bag whenever it's length is close to getting to half of it's capacity
        if self.size() < self.capacity() // 2:
            self.contract()

        counter = 0

        # Perform linear search while removing elements
        for i in range(self.size() - 1, -1, -1):
            if self.myBag[i] == element:

                # Substitute element to be removed with last element of bag
                self.myBag[i] = self.myBag[self.currentSize - 1]
                # Substitute last element of bag with None
                self.myBag[self.currentSize - 1] = None

                self.currentSize -= 1
                counter += 1

            # Exit early whenever the first None is found
            elif self.myBag[i] is None:
                break

        return counter


    # Time complexity: O(n)
    def clear(self):
        # Store capacity of previous bag
        capacity = self.capacity()

        # Delete bag
        del self.myBag

        # Create new one with the previous capacity, but none of the elements
        self.myBag = [None] * capacity
        self.currentSize = 0

        return True


    # Time complexity: O(n)
    def count(self, element):
        # Force element to be desired data type if it is valid
        if not self.validElement(element):
            return False
        else:
            element = self.dataType(element)

        counter = 0
        # Perform linear search for element
        for i in range(self.size()):
            if self.myBag[i] == element:
                counter += 1

        return counter


    # Equivalent to the length (or the amount of actual elements it has)
    # Time complexity: O(1)
    def size(self):
        return self.currentSize


    # Equivalent to how many elements it would be able to hold
    # Time complexity: O(1)
    def capacity(self):
        return len(self.myBag)


    # Time complexity: O(1)
    def isEmpty(self):
        return self.size() == 0


    # 🎆🎇🎉🎊 MAGIC METHODS 🧝‍♂️🧙‍♂️🧙‍♀️

    # String representation of this bag
    def __str__(self):
        return str(list(self))

    # Get the current size of this bag
    def __len__(self):
        return self.currentSize

    # When testing membership with the "in" operator
    def __contains__(self, el):
        return self.contains(el)

    # When this bag is added with another, return the merging of both
    def __add__(self, b2):
        if self.dataType == b2.dataType:
            tempBag = Bag(self.dataType)

            for el in self:
                tempBag.add(el)

            for el in b2:
                tempBag.add(el)

            return tempBag
        
        else:
            return None

    # When using bool() method
    def __bool__(self):
        return not self.isEmpty()

    # Generate hash by multiplying position by hash of the internal elements
    def __hash__(self):
        counter = 1
        total = 0
        for element in self:
            total += counter * hash(element)
            counter += 1

        return total % int(1E19)


    # Iterator methods
    def __iter__(self):
        self.iterationIndex = 0
        return self

    def __next__(self):
        if self.iterationIndex < self.size() and self.myBag[self.iterationIndex] is not None:
            self.iterationIndex += 1
            return self.myBag[self.iterationIndex-1]
        else:
            raise StopIteration



if __name__ == "__main__":
    bag1 = Bag(str)
    for i in range(66,90):
        bag1.add(chr(i))
        bag1.add(chr(i+1))
        bag1.add(chr(i-1))

    breakpoint()
