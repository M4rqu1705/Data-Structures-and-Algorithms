#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Was heavily inspired by the Doubly Linked List
class SinglyLinkedList:
    class Node:
        def __init__(self):
            self.value = None
            self.next = None


    def __init__(self, param = None):
        self.head = self.Node()
        self.dummy_tail = self.Node()
        self.currentSize = 0

        self.head.value = None
        self.dummy_tail.value = None

        self.head.next = None
        self.dummy_tail.next = None

        # If a parameter is integer, use it to initialize linked list size
        if isinstance(param, int):
            for i in range(param):
                self.append(None)

        # Otherwise assume param is an iterator and append all of its elements to the list
        elif param is not None:
            try:
                iter(param)

                for element in param:
                    self.append(element)
            # If iterator assumption fails, ignore param
            except:
                raise TypeError(f"Can only accept integers or iterators as initialization parameter for Singly Linked list. Received {type(param)}")



    # Time complexity: O(1)
    def append(self, element):
        # Create new node
        newNode = self.Node()
        newNode.value = element
        newNode.next = None

        # If linked list is empty ...
        if self.isEmpty():
            # Set new node in the required position
            self.head.next = newNode

            # Do some maintenance on dummy tail
            self.dummy_tail.next = self.head.next

        # ... otherwise ...
        else:
            # Set it in the required position
            self.dummy_tail.next.next = newNode

            # Do some maintenance on dummy tail
            self.dummy_tail.next = self.dummy_tail.next.next

        self.currentSize += 1

        return True


    # Time complexity: O(n)
    def insert(self, index, element):
        # Check if index is valid
        if index < 0 or index > self.size():
            raise IndexError(f"Index {index} outside of bounds for Singly Linked List of size {self.size()}")

        # Travel to the node exactly at the 'index'th position
        current_node = self.head
        i = -1
        while i < index:
            current_node = current_node.next
            i += 1

        newNode = self.Node()
        newNode.value = element
        newNode.next = current_node.next

        # Set it in the required position
        current_node.next = newNode

        # Do some maintenance on dummy tail, if necessary
        if current_node is self.dummy_tail.next:
            self.dummy_tail.next = newNode

        self.currentSize += 1
        return True


    # Time complexity: O(n)
    def remove(self, element):
        # Remove possibility of edge case early on
        if self.isEmpty():
            return False

        # Travel to the node before the one that contains the desired element
        node = self.head

        while node.next.value != element and node.next.next is not None:
            node = node.next

        # If the node's value is not the one we are looking for, we did not find
        # the desired item so we must return false
        if node.next.value != element:
            return False

        # Remove the current_node from linked list
        temp = node.next
        node.next = node.next.next
        del temp

        # If element is the last on the list, we need to do maintenance on the dummy tail
        if node.next is None:
            self.dummy_tail = node

        self.currentSize -= 1

        return True


    # Time complexity: O(n)
    def remove_all(self, element):
        # Remove possibility of edge case early on
        if self.isEmpty():
            return 0

        counter = 0
        node = self.head

        for _ in range(self.size()):
            # Travel to the node that contains the desired element
            while node.next.value != element and node.next.next is not None:
                node = node.next

            # Element was not found again, break from while loop
            if node.next.value == element:
                # Remove the current_node from linked list
                temp = node.next

                node.next = node.next.next
                del temp

                counter += 1

                # If element is the second-to-last on the list, we need to do maintenance on the dummy tail
                if node.next is None:
                    self.dummy_tail.next = node
                    break

        self.currentSize -= counter

        return counter


    # Time complexity: O(n)
    def delete(self, index):
        # Check if index is valid
        if index < 0 or index >= self.size():
            raise IndexError(f"Index {index} outside of bounds for Singly Linked List of size {self.size()}")

        # Travel to the node exactly before the 'index'th position
        node = self.head
        i = 0
        while i < index:
            node = node.next
            i += 1


        # Remove the current_node from linked list
        temp = node.next
        node.next = node.next.next
        del temp

        # If element is the last on the list, we need to do maintenance on the dummy tail
        if index == self.size() - 1:
            self.dummy_tail.next = node

        self.currentSize -= 1

        return True


    # Time complexity: O(n)
    def get(self, index):
        # Check if index is valid
        if index < 0 or index >= self.size():
            raise IndexError(f"Index {index} outside of bounds for Singly Linked List of size {self.size()}")

        # Travel to the node exactly at the 'index'th position
        node = self.head
        i = 0
        while i < index:
            node = node.next
            i += 1

        return node.next.value


    # Time complexity: O(n)
    def set(self, index, element):
        # Check if index is valid
        if index < 0 or index >= self.size():
            raise IndexError(f"Index {index} outside of bounds for Singly Linked List of size {self.size()}")

        # Travel to the node exactly at the 'index'th position
        node = self.head
        i = -1
        while i < index:
            node = node.next
            i += 1

        node.value = element

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
            return self.dummy_tail.next.value


    # Time complexity: O(n)
    def index(self, element):
        # Travel to the node that contains the desired element
        current_node = self.head.next
        i = 0
        while current_node is not None and current_node.value != element:
            current_node = current_node.next
            i += 1

        # Element was not found
        if current_node.value != element:
            return -1

        else:
            return i


    # Time complexity: O(n)
    def last_index(self, element):
        # Travel to the node that contains the desired element
        current_node = self.head.next
        match_index = -1
        i = 0

        while current_node is not None:
            if current_node.value == element:
                match_index = i
            current_node = current_node.next
            i += 1

        return match_index


    # Equivalent to the length (or the amount of actual elements it has)
    # Time complexity: O(1)
    def size(self):
        return self.currentSize


    # Time complexity: O(1)
    def isEmpty(self):
        return self.size() == 0


    # Time complexity: O(n)
    def contains(self, element):
        return self.index() != -1


    # Time complexity: O(n)
    def clear(self):
        while self.head.next is not None:
            current_node = self.head.next
            self.head.next = self.head.next.next
            del current_node

        self.dummy_tail.next = None
        self.currentSize = 0


    # 🎆🎇🎉🎊 MAGIC METHODS 🧝‍♂️🧙‍♂️🧙‍♀️

    # String representation of this linked list
    def __str__(self):
        return str(list(self))


    # Machine readable representation of this linked list
    def __repr__(self):
        return str(self)

    # Get the current size of this linked list
    def __len__(self):
        return self.currentSize


    # When testing membership with the "in" operator
    def __contains__(self, el):
        return self.contains(el)


    # When adding an object to this linked list ...
    def __add__(self, l2):
        tempList = SinglyLinkedList()
        for el in self:
            tempList.append(el)

        # Merge both Linked Lists
        if isinstance(l2, SinglyLinkedList):
            for el in l2:
                tempList.append(el)
        # Otherwise just append the element
        else:
            tempList.append(l2)

        return tempList


    # When adding this linked list to another object ...
    def __radd__(self, l1):
        tempList = SinglyLinkedList()

        # Merge both Linked Lists
        if isinstance(l1, SinglyLinkedList):
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
            tempList = SinglyLinkedList()

            # Iterate val amount of times ...
            for i in range(val):

                # while appending all elements of our linked list to the tempList
                for el in self:
                    tempList.append(el)

            return tempList
        else:
            raise TypeError("Can only multiply Singly Linked List by integers")


    # When using the [] to get the item:
    def __getitem__(self, param):
        # Enable the use of negative indices by using modulo and the size of the Singly Linked List
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
            output = SinglyLinkedList()

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
            tempList = SinglyLinkedList()

            param = sorted([index % self.size() for index in param])

            for index in param:
                tempList.append(self.get(index))

            return tempList

        else:
            raise TypeError("Can only accept integers or slices as indices for Singly Linked Lists")


    # When using the [] to set the item:
    def __setitem__(self, param, value):
        # Enable the use of negative indices by using modulo and the size of the Singly Linked List
        if isinstance(param, int):
            index = param % self.size()
            self.set(index, value)
        else:
            raise TypeError("Can only accept integers indices to set values for Singly Linked Lists")


    # When using the del operator to delete item
    def __delitem__(self, param):
        if isinstance(param, int):
            # Enable the use of negative indices by using modulo and the size of the Doubly Linked List
            index = param % self.size()
            self.delete(index)
        else:
            raise TypeError("Can only accept integers indices to delete values for Doubly Linked Lists")


    # When using bool() method
    def __bool__(self):
        return not self.isEmpty()

    def __hash__(self) -> int:
        '''Generate a hash of this Singly Linked List using `FNV1A hash
        <https://en.wikipedia.org/wiki/Fowler%E2%80%93Noll%E2%80%93Vo_hash_function>`_

        Makes a copy of this Singly Linked List and uses FNV1A hash with a little tweak (I
        use modulo 1E19 just so numbers don't get TOO big)

        Returns:
            int: This Singly Linked List's hash code

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
        self.iterationNode = self.head
        return self

    def __next__(self):
        if self.iterationNode.next is not None:
            self.iterationNode = self.iterationNode.next
            return self.iterationNode.value
        else:
            raise StopIteration

if __name__ == "__main__":
    ll1 = SinglyLinkedList()
    for i in range(65,91):
        ll1.append(chr(i))

    ll1.insert(10, 'A')
    ll1.append('A')
    print(ll1)
    breakpoint()
