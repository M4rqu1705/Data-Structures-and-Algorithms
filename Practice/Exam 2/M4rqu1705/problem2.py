#!/usr/bin/env python
# -*- coding: utf-8 -*-
from Set import Set

def makeNum(string: str) -> int:
    total = 0

    string_size = len(string)

    for i in range(len(string)):
        total += (string_size - i) * ord(string[i])

    return total


def isSorted(L):

    # Begin with the first node (not the header)
    current_node = L.head.next
    i = 0

    # Use `i` as an indicator of iteration progress through the singly-linked list.
    # (Can't proceed until the end because we always need to compare the current_node with the next
    #   one. That's why I use L.size() - 1)
    while i < L.size() - 1:
        # If the current value is greater than the next value ...
        if makeNum(current_node.value) > makeNum(current_node.next.value):
            # ... the list is not sorted in INCREASING order
            return False

        # Otherwise, proceed to the next element
        current_node = current_node.next
        i += 1

    # If we got to the end and there was no error, the list is sorted
    return True


def removeDuplicates(L):
    # Set that will help us efficiently identify repeated elements
    encountered = Set()

    current_node = L.head

    # I am assuming that the Singly-Linked List does not have a dummy tail
    while current_node.next is not None:
        # If the next node's value was previously seen ...
        if current_node.next.value in encountered:
            # ... link our next pointer with the next node's next node and then delete the next node
            next_node = current_node.next
            current_node.next = current_node.next.next
            del next_node

        # Otherwise, simply add it's value to the encountered set and continue to the next node
        else:
            encountered.add(current_node.next.value)
            current_node = current_node.next

            
    return L
