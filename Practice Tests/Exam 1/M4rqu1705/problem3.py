#!/usr/bin/env python 
# -*- coding: utf-8 -*-

class customArrayList(list):

    # Python lists do not have last_index method, so I'm implementing one now for my custom Array List
    # Time complexity: O(n)
    def last_index(self, X):
        for i in range(len(self)):
            index = len(self) - 1 - i

            if X == self[index]:
                return index

        return -1


    # Time complexity: O(n³), n = len(self)
    def removeDuplicates(self):
        i = 0

        # Using while loop instead of for loop since the size of this list is frequently changing, and the range generator does not notice these changes in size
        # O(n)
        while i < len(self):
            # Get the element at the current index
            element = self[i]

            # O(n)
            last_index = self.last_index(element)

            # O(n)
            # Keep removing the last copy of element X while the first_index (which will always be i) is not the same as the last_index
            while i != last_index:
                # O(n)
                # Remove the last copy
                del self[last_index]

                # O(n)
                # Check for the last index once again
                last_index = self.last_index(element)
            
            # Increment variable of iteration / first_index
            i += 1


class customDynamicBag(list):

    # Time Complexity: O(n*m²), n = len(B), m = len(self)
    def bagAnalyzer(self, B):
        # Prepare an output array in which to hold each element's count
        output = []

        # O(n)
        # Iterate through bag B
        for element in B:
            # O(m)
            # Prepare a copy of self as to not change its contents
            copy = self[:]
            copies_counter = 0

            # O(m)
            while True:
                try:
                    # Try to remove element from copy
                    # O(m)
                    copy.remove(element)
                    # If it was successful, then we can increase the counter
                    copies_counter += 1
                except ValueError:
                    # While loop ends when remove operation fails
                    break

            # Append the latest element's counter to the output array
            output.append(copies_counter)

        return output




if __name__ == "__main__":
    L = customArrayList()

    L.append(1)
    L.append(0)
    L.append(4)
    L.append(3)
    L.append(1)
    L.append(1)
    L.append(2)
    L.append(4)

    print("Remove duplicates:")
    print(f'Before: {L}')
    L.removeDuplicates()
    print(f'After: {L}')
    print()

    M = customDynamicBag()
    M.append(1)
    M.append(4)
    M.append(5)
    M.append(4)
    M.append(11)
    M.append(4)
    M.append(0)
    M.append(1)

    B = customDynamicBag()
    B.append(1)
    B.append(8)
    B.append(1)
    B.append(4)

    print("Bag Analyzer:")
    print(M.bagAnalyzer(B))
    print()

