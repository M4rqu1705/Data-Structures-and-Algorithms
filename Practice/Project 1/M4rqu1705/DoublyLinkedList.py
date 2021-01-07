#!/usr/bin/env python
# -*- coding: utf-8 -*-

class DoublyLinkedList:
    class Node:
        def __init__(self):
            self.value = None
            self.next = None
            self.prev = None


    def __init__(self, param = None):
        self.head = self.Node()
        self.tail = self.Node()
        self.currentSize = 0

        self.head.value = None
        self.tail.value = None

        self.head.prev = None
        self.head.next = self.tail
        self.tail.prev = self.head
        self.tail.next = None

        # If a parameter is integer, use it to initialize linked list size
        if isinstance(param, int):
            for i in range(param):
                self.append(None)

        # Otherwise assume param is an iterator and append all of its elements to the list
        else:
            try:
                iter(param)

                for element in param:
                    self.append(element)
            # If iterator assumption fails, ignore param
            except:
                pass


    # 👜🎒 LINKED LIST ADT METHODS 💼🏎

    # Time complexity: O(1)
    def append(self, element):
        # Create new node
        newNode = self.Node()
        newNode.value = element

        # Change it's prev and next pointers
        newNode.prev = self.tail.prev
        newNode.next = self.tail

        # Do some maintenance on the surrounding nodes
        self.tail.prev.next = newNode
        self.tail.prev = newNode

        self.currentSize += 1
        return True


    # Time complexity: O(n)
    def insert(self, index, element):
        # Check if index is valid
        if 0 > index or index > self.size():
            raise IndexError(f"Index {index} outside of bounds for Doubly Linked List of size {self.size()}")

        # Travel to the node exactly at the 'index'th position
        current_node = self.head
        i = -1
        while i < index:
            current_node = current_node.next
            i += 1

        # Create new node
        newNode = self.Node()
        newNode.value = element

        # Change it's prev and next pointers
        newNode.prev = current_node.prev
        newNode.next = current_node

        # Do some maintenance on the surrounding nodes
        current_node.prev.next = newNode
        current_node.prev = newNode

        self.currentSize += 1
        return True


    # Time complexity: O(n)
    def remove(self, element):
        # Travel to the node that contains the desired element
        current_node = self.head.next
        while current_node.value != element and current_node is not self.tail:
            current_node = current_node.next

        # Element was not found
        if current_node is self.tail:
            return False

        # Do some maintenance on the surrounding nodes
        current_node.prev.next = current_node.next
        current_node.next.prev = current_node.prev

        del current_node

        self.currentSize -= 1
        return True


    # Time complexity: O(n)
    def remove_all(self, element):
        counter = 0
        current_node = self.head.next
        
        while current_node is not self.tail:
            # Travel to the node that contains the desired element
            while current_node.value != element and current_node is not self.tail:
                current_node = current_node.next

            # Element was not found
            if current_node is self.tail:
                return counter

            # Do some meaintenance on the surrounding nodes
            current_node.prev.next = current_node.next
            current_node.next.prev = current_node.prev
            temp = current_node.next

            del current_node

            current_node = temp

            counter += 1

        self.currentSize -= counter
        return counter


    # Time complexity: O(n)
    def delete(self, index):
        # Check if index is valid
        if 0 > index or index >= self.size():
            raise IndexError(f"Index {index} outside of bounds for Doubly Linked List of size {self.size()}")

        # Travel to the node exactly at the 'index'th position
        current_node = self.head
        i = -1
        while i < index:
            current_node = current_node.next
            i += 1

        # Do some meaintenance on the surrounding nodes
        current_node.prev.next = current_node.next
        current_node.next.prev = current_node.prev

        del current_node

        self.currentSize -= 1
        return True


    # Time complexity: O(n)
    def get(self, index):
        # Check if index is valid
        if 0 > index or index >= self.size():
            raise IndexError(f"Index {index} outside of bounds for Doubly Linked List of size {self.size()}")

        # Travel to the node exactly at the 'index'th position
        current_node = self.head
        i = -1
        while i < index:
            current_node = current_node.next
            i += 1

        return current_node.value


    # Time complexity: O(n)
    def set(self, index, element):
        # Check if index is valid
        if 0 > index or index >= self.size():
            raise IndexError(f"Index {index} outside of bounds for Doubly Linked List of size {self.size()}")

        # Travel to the node exactly at the 'index'th position
        current_node = self.head
        i = -1
        while i < index:
            current_node = current_node.next
            i += 1

        current_node.value = element

        return True


    # Time complexity: O(1)
    def get_first(self):
        if self.isEmpty():
            return None
        # Can only return first element if linked list is not empty!
        else:
            return self.head.next.value


    # Time complexity: O(1)
    def get_last(self):
        if self.isEmpty():
            return None
        # Can only return last element if linked list is not empty!
        else:
            return self.tail.prev.value


    # Time complexity: O(n)
    def index(self, element):
        # Travel to the node that contains the desired element
        current_node = self.head.next
        i = 0
        while current_node.value != element and current_node is not self.tail:
            current_node = current_node.next
            i += 1

        # Element was not found
        if current_node is self.tail:
            return -1
        
        else:
            return i


    # Time complexity: O(n)
    def last_index(self, element):
        # Travel to the node that contains the desired element
        current_node = self.tail.prev
        i = self.size() - 1
        while current_node.value != element and current_node is not self.head:
            current_node = current_node.prev
            i -= 1

        # Element was not found
        if current_node is self.head:
            return -1
        
        else:
            return i


    # Equivalent to the length (or the amount of actual elements it has)
    # Time complexity: O(1)
    def size(self):
        return self.currentSize

    
    # Time complexity: O(1)
    def isEmpty(self):
        return self.size() == 0


    # Time complexity: O(n)
    def contains(self, element):
        # Travel to the node that contains the desired element
        current_node = self.head.next
        while current_node.value != element and current_node is not self.tail:
            current_node = current_node.next

        # Element was not found
        if current_node is self.tail:
            return False

        return True


    # Time complexity: O(n)
    def clear(self):
        while self.head.next is not self.tail:
            self.head.next = self.head.next.next
            del self.head.next.prev
            self.head.next.prev = self.head

        self.currentSize = 0


    # 🎆🎇🎉🎊 MAGIC METHODS 🧝‍♂️🧙‍♂️🧙‍♀️

    # String representation of this linked list
    def __str__(self):
        return str(list(self))


    # Machine readable representation of this linked list
    def __repr__(self):
        return str(list(self))

    # Get the current size of this linked list
    def __len__(self):
        return self.currentSize


    # When testing membership with the "in" operator
    def __contains__(self, el):
        return self.contains(el)


    # When adding an object to this linked list ...
    def __add__(self, l2):
        tempList = DoublyLinkedList()
        for el in self:
            tempList.append(el)

        # Merge both Linked Lists
        if isinstance(l2, DoublyLinkedList):
            for el in l2:
                tempList.append(el)
        # Otherwise just append the element
        else:
            tempList.append(l2)

        return tempList


    # When adding this linked list to another object ...
    def __radd__(self, l1):
        tempList = DoublyLinkedList()

        # Merge both Linked Lists
        if isinstance(l1, DoublyLinkedList):
            for el in l1:
                tempList.append(el)

        # Otherwise just append the element
        else:
            tempList.append(l1)

        for el in self:
            tempList.append(el)

        return tempList


    # When this linked list is multiplied by an integer, then it should be repeated that amount of time
    def __mul__(self, val):
        if isinstance(val, int):
            tempList = DoublyLinkedList()

            # Iterate val amount of times ...
            for i in range(val):

                # while appending all elements of our linked list to the tempList
                for el in self:
                    tempList.append(el)

            return tempList
        else:
            raise TypeError("Can only multiply Doubly Linked List by integers")


    # When using the [] to get the item:
    def __getitem__(self, param):
        # Enable the use of negative indices by using modulo and the size of the Doubly Linked List
        if isinstance(param, int):
            index = param % self.size()
            return self.get(index)

        # Enable the use of slices for more advanced linked list operations (O(n))
        elif isinstance(param, slice):
            start = param.start or 0
            end = param.stop or self.size()
            step = param.step or 1

            # Travel to the "start"th node
            current_node = self.head
            i = -1
            while i < start:
                current_node = current_node.next
                i += 1

            # Prepare output linked list
            output = DoublyLinkedList()

            # Append all relevant data to the output linked list
            while i < end:
                output.append(current_node.value)
                j = 0
                while j < step:
                    current_node = current_node.next
                    j += 1
                i += step

            return output

        # Enable the use of specific tuples or lists of int type indices (O(n log(n) + n * m))
        elif isinstance(param, tuple) or isinstance(param, list) and all(isinstance(el, int) for el in param):
            tempList = DoublyLinkedList()

            param = sorted([index % self.size() for index in param])

            for index in param:
                tempList.append(self.get(index))

            return tempList

        else:
            raise TypeError("Can only accept integers or slices as indices for Doubly Linked Lists")


    # When using the [] to set the item:
    def __setitem__(self, param, value):
        # Enable the use of negative indices by using modulo and the size of the Doubly Linked List
        if isinstance(param, int):
            index = param % self.size()
            self.set(index, value)
        else:
            raise TypeError("Can only accept integers indices to set values for Doubly Linked Lists")


    # When using bool() method
    def __bool__(self):
        return not self.isEmpty()

    # Generate hash by multiplying position by hash of the internal elements
    def __hash__(self):
        # Will help differentiate lists with same elements in different orders
        counter = 1
        # Accumulates the sum of the previous calculation, and will contain the final hash
        total = 0

        for element in self:
            # counter is squared to distinguish hashes that have similar elements even more
            total += counter * counter * hash(element)
            counter += 1
            # Cap total at a maximum of 1E19 to prevent nubers getting out of hand
            total %= int(1E19)

        return total


    # Iterator methods
    def __iter__(self):
        self.iterationNode = self.head
        return self

    def __next__(self):
        if self.iterationNode.next is not self.tail:
            self.iterationNode = self.iterationNode.next
            return self.iterationNode.value
        else:
            raise StopIteration

if __name__ == "__main__":
    ll1 = DoublyLinkedList(str)
    for i in range(65,91):
        ll1.append(chr(i))

    breakpoint()
