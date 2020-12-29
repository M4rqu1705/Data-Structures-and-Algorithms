#!/usr/bin/env python
# -*- coding: utf-8 -*-
class DoublyLinkedList:
    class Node:
        def __init__(self):
            self.value = None
            self.next = None
            self.prev = None


    def __init__(self, dataType):
        self.head = self.Node()
        self.tail = self.Node()
        self.currentSize = 0
        self.dataType = dataType

        self.head.value = None
        self.tail.value = None

        self.head.prev = None
        self.head.next = self.tail
        self.tail.prev = self.head
        self.tail.next = None


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


    # 👜🎒 LINKED LIST ADT METHODS 💼🏎

    # Time complexity: O(1)
    def append(self, element):
        # Force element to be desired data type if it is valid
        if not self.validElement(element):
            return False
        else:
            element = self.dataType(element)

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
        # Force element to be desired data type if it is valid
        if not self.validElement(element):
            return False
        else:
            element = self.dataType(element)

        # Check if index is valid
        if 0 > index or index > self.size():
            return False

        # Travel to the node exactly at the 'index'th position
        ith_node = self.head
        i = -1
        while i < index:
            ith_node = ith_node.next
            i += 1

        # Create new node
        newNode = self.Node()
        newNode.value = element

        # Change it's prev and next pointers
        newNode.prev = ith_node.prev
        newNode.next = ith_node

        # Do some maintenance on the surrounding nodes
        ith_node.prev.next = newNode
        ith_node.prev = newNode

        self.currentSize += 1
        return True


    # Time complexity: O(n)
    def remove(self, element):
        # Force element to be desired data type if it is valid
        if not self.validElement(element):
            return False
        else:
            element = self.dataType(element)

        # Travel to the node that contains the desired element
        ith_node = self.head
        while ith_node.value != element and ith_node is not self.tail:
            ith_node = ith_node.next

        # Element was not found
        if ith_node is self.tail:
            return False

        # Do some meaintenance on the surrounding nodes
        ith_node.prev.next = ith_node.next
        ith_node.next.prev = ith_node.prev

        del ith_node

        self.currentSize -= 1
        return True


    # Time complexity: O(n)
    def remove_all(self, element):
        # Force element to be desired data type if it is valid
        if not self.validElement(element):
            return 0
        else:
            element = self.dataType(element)

        counter = 0
        ith_node = self.head
        
        while ith_node is not self.tail:
            # Travel to the node that contains the desired element
            while ith_node.value != element and ith_node is not self.tail:
                ith_node = ith_node.next

            # Element was not found
            if ith_node is self.tail:
                return counter

            # Do some meaintenance on the surrounding nodes
            ith_node.prev.next = ith_node.next
            ith_node.next.prev = ith_node.prev
            temp = ith_node.next

            del ith_node

            ith_node = temp

            counter += 1

        self.currentSize -= counter
        return counter


    # Time complexity: O(n)
    def delete(self, index):
        # Check if index is valid
        if 0 > index or index > self.size():
            return False

        # Travel to the node exactly at the 'index'th position
        ith_node = self.head
        i = -1
        while i < index:
            ith_node = ith_node.next
            i += 1

        # Do some meaintenance on the surrounding nodes
        ith_node.prev.next = ith_node.next
        ith_node.next.prev = ith_node.prev

        del ith_node

        self.currentSize -= 1
        return True


    # Time complexity: O(n)
    def get(self, index):
        # Check if index is valid
        if 0 > index or index > self.size():
            return None

        # Travel to the node exactly at the 'index'th position
        ith_node = self.head
        i = -1
        while i < index:
            ith_node = ith_node.next
            i += 1

        return ith_node.value


    # Time complexity: O(n)
    def set(self, index, element):
        # Force element to be desired data type if it is valid
        if not self.validElement(element):
            return False
        else:
            element = self.dataType(element)

        # Travel to the node exactly at the 'index'th position
        ith_node = self.head
        i = -1
        while i < index:
            ith_node = ith_node.next
            i += 1

        ith_node.value = element

        return True


    # Time complexity: O(1)
    def get_first(self):
        return self.head.next.value


    # Time complexity: O(1)
    def get_last(self):
        return self.tail.prev.value


    # Time complexity: O(n)
    def index(self, element):
        # Force element to be desired data type if it is valid
        if not self.validElement(element):
            return -1
        else:
            element = self.dataType(element)

        # Travel to the node that contains the desired element
        ith_node = self.head
        i = -1
        while ith_node.value != element and ith_node is not self.tail:
            ith_node = ith_node.next
            i += 1

        # Element was not found
        if ith_node is self.tail:
            return -1
        
        else:
            return i


    # Time complexity: O(n)
    def last_index(self, element):
        # Force element to be desired data type if it is valid
        if not self.validElement(element):
            return -1
        else:
            element = self.dataType(element)

        # Travel to the node that contains the desired element
        ith_node = self.tail
        i = self.size()
        while ith_node.value != element and ith_node is not self.head:
            ith_node = ith_node.prev
            i -= 1

        # Element was not found
        if ith_node is self.head:
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
        # Force element to be desired data type if it is valid
        if not self.validElement(element):
            return False
        else:
            element = self.dataType(element)

        # Travel to the node that contains the desired element
        ith_node = self.head
        while ith_node.value != element and ith_node is not self.tail:
            ith_node = ith_node.next

        # Element was not found
        if ith_node is self.tail:
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

    # When this linked list is added with another, return the merging of both
    def __add__(self, l2):
        if self.dataType == l2.dataType:
            tempList = DoublyLinkedList(self.dataType)

            for el in self:
                tempList.add(el)

            for el in l2:
                tempList.add(el)

            return tempList
        
        else:
            return None


    # When using the [] to get the item:
    def __getitem__(self, index):
        if isinstance(index, int):
            return self.get(index)
        elif isinstance(index, slice):
            start = index.start or 0
            end = index.stop or self.size()
            step = index.step or 1

            # Travel to the "start"th node
            ith_node = self.head
            i = -1
            while i < start:
                ith_node = ith_node.next
                i += 1

            # Prepare output linked list
            output = DoublyLinkedList(self.dataType)

            # Append all relevant data to the output linked list
            while i < end:
                output.append(ith_node.value)
                j = 0
                while j < step:
                    ith_node = ith_node.next
                    j += 1
                i += step

            return output
        else:
            return None


    # When using the [] to set the item:
    def __setitem__(self, index, value):
        self.set(index, value)


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
