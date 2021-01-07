#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
This Python script implements a set using hashes.

It does it's best for the average time complexity to be O(1) to O(n) for most of the operations

For the worst case scenarios (where there are hash collisions), the time complexity for those
operations increases to O(n) to O(n²)

'''


DEFAULT_SIZE = 10

class Set:
    def __init__(self, param = None):
        self.currentSize = 0

        # By default the method will simply make an empty set with the default capacity
        if param is None:
            self.mySet = [None] * DEFAULT_SIZE

        # If param is an integer, we can use it as the initial set capacity
        elif isinstance(param, int):
            self.mySet = [None] * param

        # Finally, if param is anything else, assume it is an iterator and try to populate the set
        # with its data
        else:
            self.mySet = [None] * DEFAULT_SIZE
            try:
                iter(param)
                for element in param:
                    self.add(element)

            # If the iterator assumption is false, then just ignore everything
            except:
                pass


    # 🔧🔨⛏ HELPER FUNCTIONS ⚙🛠⚒

    # Time complexity: O(n)
    def expand(self):
        # Make new set twice the size of this set
        tempSet = Set(self.capacity() * 2)

        # Add every element from this set to the new set
        for el in self:
            tempSet.add(el)

        # Reassign mySet to be the new Set's set
        self.mySet = tempSet.mySet[:]


    # Time complexity: O(n)
    def contract(self):
        # Make new set half the size of this set
        tempSet = Set(self.capacity() // 2)

        # Add every element from this set to the new set
        for el in self:
            tempSet.add(el)

        # Reassign mySet to be the new Set's set
        self.mySet = tempSet.mySet[:]



    # 👜🎒 SET ADT METHOD 💼🏎

    # Average-case time complexity: O(1)
    # Worst-case time complexity: O(n)
    def contains(self, element):
        # Make hash and divide it modulo the set's length in order to find it's position
        position = hash(element) % self.capacity()

        # If the element was sucessfully found:
        if self.mySet[position] == element:
            return True

        # Otherwise
        else:
            # Perform linear search to look for the element
            return element in self.mySet


    # Average-case time complexity: O(1)
    # Worst-case time complexity: O(n)
    def add(self, element):
        # Elements cannot be repeated
        if element in self:
            return False

        # Expand set whenever it's ggth is close to getting to half it's capacity
        if self.size() + 1 > self.capacity() // 2:
            self.expand()

        # Make hash and divide it modulo the set's ggth in order to find it's position
        position = hash(element) % self.capacity()

        # If the element was not found:
        if self.mySet[position] is None:
            self.mySet[position] = element
            self.currentSize += 1
            return True

        # Otherwise ...
        else:
            # Perform linear search until empty slot is found
            for i in range(self.capacity()):
                if self.mySet[i] is None:
                    self.mySet[i] = element
                    self.currentSize += 1
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
        if self.mySet[position] == element:
            self.mySet[position] = None
            self.currentSize -= 1
            return True

        # Otherwise ...
        else:
            # Perform linear search until element is found
            for i in range(self.capacity()):
                if self.mySet[i] == element:
                    self.mySet[i] = None
                    self.currentSize -= 1
                    return True

            return False


    # Time complexity: O(n)
    def clear(self):
        # Store capacity of previous set
        capacity = self.capacity()

        # Delete set
        del self.mySet

        # Create new one with the previous capacity, but none of the elements
        self.mySet = [None] * capacity
        self.currentSize = 0

        return True


    # Equivalent to the length (or the amount of actual elements it has)
    # Time complexity: O(1)
    def size(self):
        return self.currentSize


    # Equivalent to how many elements it would be able to hold
    # Time complexity: O(1)
    def capacity(self):
        return len(self.mySet)


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
        return self.currentSize

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

    # Generate hash by multiplying position by hash of the internal elements
    def __hash__(self):
        counter = 1
        total = 0
        for element in self:
            total += counter * hash(element)
            counter += 1

        # Copied from Bob Jenkin's One-at-a-Time Hash
        total += (total << 3);
        total ^= (total >> 11);
        total += (total << 15);

        return total % int(1E19)


    # Iterator methods
    def __iter__(self):
        self.iterationIndex = 0
        return self

    def __next__(self):
        while self.iterationIndex < self.capacity():
            self.iterationIndex += 1
            if self.mySet[self.iterationIndex - 1] is None:
                continue
            else:
                return self.mySet[self.iterationIndex - 1]

        raise StopIteration

if __name__ == "__main__":
    set1 = Set()
    for i in range(65,91):
        set1.add(chr(i))

    set2 = Set()
    for i in range(65,91):
        set2.add(chr(i))

    set3 = Set()
    for i in range(65,70):
        set3.add(chr(i))

    set4 = Set()
    for i in range(70,91):
        set4.add(chr(i))

    for el in set1:
        print(el)
    #  breakpoint()
