#!/usr/bin/env python
# -*- coding: utf-8 -*-

class Node:
    def __init__(self, v, n):
        self.val = v
        self.next = n

class LinkedList:
    def __init__(self):
        self.linked_list = None
        self.size = 0

    def add(self, val):
        if self.linked_list is None:
            self.linked_list = Node(val, None)

        else:
            pointer = self.linked_list

            while pointer.next is not None:
                pointer = pointer.next

            pointer.next = Node(val, None)

        self.size += 1

    def insert(self, val, pos):
        pointer = self.linked_list
        prev_pointer = self.linked_list

        if 0 > pos:
            pos = 0
        elif self.size < pos:
            pos = self.size

        for i in range(pos):
            prev_pointer = pointer
            pointer = pointer.next

        prev_pointer.next = Node(val, pointer)

        self.size += 1

    def print(self):
        pointer = self.linked_list

        while pointer.next is not None:
            print(f'{pointer.val} -> ', end='')
            pointer = pointer.next

        print(f"{pointer.val}")




if __name__ == "__main__":
    ll = LinkedList()
    ll.add(1)
    ll.add(2)
    ll.insert(4, 0)
    ll.add(3)

    ll.print()

