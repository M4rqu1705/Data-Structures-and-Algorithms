#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
This Python script implements a set keeping the elements in order

It's operations time complexity ranges from O(log(n)) to O(n²)

'''


class Set:
    def __init__(self, dataType):
        self.mySet = []
        self.mySetHashes = []
        self.dataType = dataType


    # 🔧🔨⛏ HELPER FUNCTIONS ⚙🛠⚒

    def validElement(self, element):
        # Check if set has correct data type
        if not isinstance(element, self.dataType):
            # If it is not, try to force it
            try:
                element = self.dataType(element)
                return True
            # If it cannot be forced, then element cannot be in set
            except:
                return False
        else:
            return True

    # It's a static method since it doesn't matter if it is called by an instance of the class or the class itself
    @staticmethod
    def binarySearch(element, array):
        start, end = 0, len(array)
        mid = (start + end) // 2

        while start != end:
            #  breakpoint()
            #  print("Inside binary search")
            if array[mid] > element:
                end = mid
                mid = (start + end) // 2
            elif array[mid] < element:
                start = mid + 1
                mid = (start + end) // 2
            else:
                return mid

        return -1


    # 👜🎒 SET ADT METHOD 💼🏎

    # Time complexity: O(log(n))
    def contains(self, element):
        # Force element to be desired data type if it is valid
        if not self.validElement(element):
            return False
        else:
            element = self.dataType(element)

        # Perform binary search to look for element
        position = self.binarySearch(hash(element), self.mySetHashes)

        return position >= 0



    # Time complexity: O(n)
    def add(self, element):
        # Force element to be desired data type if it is valid
        if not self.validElement(element):
            return False
        else:
            element = self.dataType(element)

        # Elements cannot be repeated
        if element in self:
            return False

        elementHash = hash(element)

        # Perform linear search to find where to put the element
        index = -1

        if self.isEmpty():
            self.mySet.append(element)
            self.mySetHashes.append(elementHash)
            return True


        if self.mySetHashes[0] > elementHash:
            index = 0
        elif self.mySetHashes[-1] < elementHash:
            index = self.size()
        else:
            for i in range(self.size() - 1):
                if self.mySetHashes[i] < elementHash and elementHash < self.mySetHashes[i + 1]:
                    index = i+1
                    break

        # Insert element to set
        self.mySet.insert(index, element)
        self.mySetHashes.insert(index, elementHash)
        return True


    # Time complexity: O(n)
    def remove(self, element):
        # Force element to be desired data type if it is valid
        if not self.validElement(element):
            return False
        else:
            element = self.dataType(element)

        # Element must be inside the set in order to be removed
        if element not in self:
            return False

        elementHash = hash(element)

        # Perform binary search to look for element
        position = self.binarySearch(elementHash, self.mySetHashes)

        del self.mySet[position]
        del self.mySetHashes[position]

    # Time complexity: O(n)
    def clear(self):
        # Delete set
        del self.mySet
        del self.mySetHashes
        # Create new empty set
        self.mySet = []
        self.mySetHashes = []
        return True


    # Equivalent to the length (or the amount of actual elements it has)
    # Time complexity: O(1)
    def size(self):
        return len(self.mySet)

    # Time complexity: O(1)
    def isEmpty(self):
        return self.size() == 0

    # Time complexity: O(n²)
    def union(self, s2):
        # Check if sets have the same types
        if self.dataType != s2.dataType:
            return None

        s3 = Set(self.dataType)

        # Add all of self's and s2's elements to s3
        for el in self:
            s3.add(el)

        for el in s2:
            s3.add(el)

        return s3


    # Time complexity: O(n² log(n))??
    def intersection(self, s2):
        return self.difference(self.difference(s2))

    # Time complexity: O(n² log(n)) ??
    def difference(self, s2):
        # Check if sets have the same types
        if self.dataType != s2.dataType:
            return None

        s3 = Set(self.dataType)

        # Add every element from self to s3 ...
        for el in self:
            s3.add(el)

        # but then remove any common elements between s3 and s2
        for el in s2:
            if el in s3:
                s3.remove(el)

        return s3

    # Time complexity: O(n log(n))
    def subset(self, s2):
        # Check if sets have the same types
        if self.dataType != s2.dataType:
            return None

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
        return self.size()

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

        return total % int(1E19)


    # Iterator methods
    def __iter__(self):
        self.iterationIndex = 0
        return self

    def __next__(self):
        if self.iterationIndex < self.size():
            self.iterationIndex += 1
            return self.mySet[self.iterationIndex - 1]

        raise StopIteration
    

if __name__ == "__main__":
    set1 = Set(str)
    for i in range(65,91):
        set1.add(chr(i))

    set2 = Set(str)
    for i in range(65,91):
        set2.add(chr(i))

    set3 = Set(str)
    for i in range(65,70):
        set3.add(chr(i))

    set4 = Set(str)
    for i in range(70,91):
        set4.add(chr(i))

    for i in range(len(set1.mySet)-1):
        if set1.mySetHashes[i] > set1.mySetHashes[i+1]:
            print("Error!")
            exit()

    breakpoint()
