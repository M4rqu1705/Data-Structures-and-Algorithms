#!/usr/bin/env python
# -*- coding: utf-8 -*-
import random
DEFAULT_SIZE = 10

class Set:
    def __init__(self, dataType, initial_capacity = DEFAULT_SIZE):
        self.currentSize = 0
        self.mySet = [None] * initial_capacity
        self.dataType = dataType

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

    def contains(self, element):
        if not self.validElement(element):
            return False
        else:
            element = self.dataType(element)

        # Make hash and divide it modulo the set's length in order to find it's position
        position = hash(element) % len(self.mySet)

        # If the element was sucessfully found:
        if self.mySet[position] == element:
            return True

        # Otherwise
        else:
            # Perform linear search to look for the element
            return element in self.mySet

    def expandSet(self):
        # Make new set twice the size of this set
        #  print(f"Expanding set from {len(self.mySet)} to {len(self.mySet) * 2}")
        tempSet = Set(self.dataType, len(self.mySet) * 2)

        # Add every element from this set to the new set
        for el in self.mySet:
            tempSet.add(el)

        # Reassign mySet to be the newSet's set
        self.currentSize = tempSet.currentSize
        self.mySet = tempSet.mySet
        


    def add(self, element):
        if not self.validElement(element):
            return False
        else:
            element = self.dataType(element)

        # Elements cannot be repeated
        if self.contains(element):
            return False

        # Expand set whenever it's length is close to getting to half it's capacity
        if self.currentSize + 1 > len(self.mySet) // 2:
            self.expandSet()

        position = hash(element) % len(self.mySet)

        if self.mySet[position] is None:
            self.mySet[position] = element
            self.currentSize += 1
            return True

        else:
            for i in range(len(self.mySet)):
                if self.mySet[i] is None:
                    self.mySet[i] = element
                    self.currentSize += 1
                    return True

    def remove(self, element):
        if not self.validElement(element):
            return False
        else:
            element = self.dataType(element)

        # Element must be inside the set in order to be removed
        if not self.contains(element):
            return False

        position = hash(element) % len(self.mySet)

        if self.mySet[position] == element:
            self.mySet[position] = None
            self.currentSize -= 1
            return True

        else:
            # Perform linear search to look for the element
            for i in range(len(self.mySet)):
                if self.mySet[i] == element:
                    self.mySet[i] = None
                    self.currentSize -= 1
                    return True
            
            return False
        
        
    def clear(self):
        capacity = len(self.mySet)
        del self.mySet
        self.mySet = [None] * capacity
        self.currentSize = 0
        
        return True

    def size(self):
        return self.currentSize

    def isEmpty(self):
        return self.size() == 0

    def union(self, s2):
        pass
    
if __name__ == "__main__":
    newSet = Set(str)
    for i in range(65,91):
        newSet.add(chr(i))

    print(newSet.mySet)
    print(newSet.size())

    for i in range(65,91):
        newSet.remove(chr(i))
    print(newSet.mySet)
    print(newSet.size())
