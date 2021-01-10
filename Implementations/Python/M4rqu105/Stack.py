#!/usr/bin/env python
# -*- coding: utf-8 -*-
from DoublyLinkedList import DoublyLinkedList

class Stack:

    class Node:
        def __init__(self):
            self.next = None
            self.value = None


    def __init__(self):
        self.head = self.Node()
        self.currentSize = 0


    # Time complexity: O(1)
    def push(self, element):
        newNode = self.Node()
        newNode.value = element

        newNode.next = self.head.next
        self.head.next = newNode

        self.currentSize += 1

        return True


    # Time complexity: O(1)
    def pop(self):
        if self.isEmpty():
            return None

        else:
            removedNode = self.head.next
            value = removedNode.value

            self.head.next = self.head.next.next

            del removedNode
            self.currentSize -= 1

            return value


    # Time complexity: O(1)
    def top(self):
        if self.isEmpty():
            return None
        else:
            return self.head.next.value


    # Time complexity: O(1)
    def size(self):
        return self.currentSize


    # Time complexity: O(1)
    def isEmpty(self):
        return self.size() == 0


    # Time complexity: O(n)
    def clear(self):
        while not self.isEmpty():
            self.pop()


    # Time complexity: O(n)
    def copy(self):
        tempStack = Stack()
        copy = Stack()

        # Transfer all contents of self to a tempStack
        while not self.isEmpty():
            tempStack.push(self.pop())

        # Transfer all contents back to self, but also to copy
        while not tempStack.isEmpty():
            self.push(tempStack.top())
            copy.push(tempStack.pop())

        return copy


    # Time complexity: O(n)
    def __str__(self):
        copy = self.copy()

        elements = DoublyLinkedList()

        while not copy.isEmpty():
            elements.append(copy.pop())

        return '[' + ', '.join(elements) + ']'


    # Time complexity: O(n)
    def __repr__(self):
        return str(self)


    # Time complexity: O(1)
    def __len__(self):
        return self.size()


    # Time complexity: O(n + m)
    def __add__(self, param):
        if isinstance(param, Stack):
            mergedStack = Stack()

            tempStack = Stack()

            s1 = self.copy()
            while not s1.isEmpty():
                tempStack.push(s1.pop())

            if isinstance(param, Stack):
                s2 = param.copy()
                while not s2.isEmpty():
                    tempStack.push(s2.pop())

            else:
                tempStack.push(param)

            while not tempStack.isEmpty():
                mergedStack.push(tempStack.pop())

            return mergedStack
        else:
            raise TypeError("Can only add stacks with stacks")


    def __hash__(self) -> int:
        '''Generate a hash of this Stack using `FNV1A hash
        <https://en.wikipedia.org/wiki/Fowler%E2%80%93Noll%E2%80%93Vo_hash_function>`_

        Makes a copy of this Stack and uses FNV1A hash with a little tweak (I
        use modulo 1E19 just so numbers don't get TOO big)

        Returns:
            int: This Stack's hash code

        Hint:
            Time complexity: O(n)
        
        '''
        total = 2166136261
            
        copy = self.copy()

        while not copy.isEmpty():
            total *= 16777619
            total ^= hash(copy.pop())
            # A little extra just to prevent numbers from getting tooo big
            total % int(1E19)

        return total


if __name__ == "__main__":
    pesante_rosa = Stack()
    pesante_rosa.push("Maribel")
    pesante_rosa.push("Taimí")
    pesante_rosa.push("Zakira")
    pesante_rosa.push("Luis")

    pesante_colon = Stack()
    pesante_colon.push("Sofía")
    pesante_colon.push("Marcos")
    pesante_colon.push("Darlene")
    pesante_colon.push("Paco")

    print( pesante_rosa + pesante_colon )

    breakpoint()
