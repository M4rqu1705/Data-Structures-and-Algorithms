#!/usr/bin/env python
# -*- coding: utf-8 -*-

def a():
    # [20, 28, 24, 21, 22]

    return 4

def b():
    # [20, 28]

    return 1

def c():
    # POST ORDER
    # 
    # visit left
    # visit right
    # visit current node

    return [10, 18, 15, 22, 21, 24, 30, 28, 20]

def d():
    # The for loop goes from 0 to the lenth of buckets
    #
    # If the buckets are implemented with an Array List, getting the ith element
    # is O(1)
    #
    # If the buckets are implemented with a Linked List, getting the ith element
    # is O(n)
    #
    # Using that n = buckets.length ...
    #
    # Assuming that the buckets are implemented with an Array List, the time
    # complexity of this function is O(n)
    #
    # On the other hand, if the buckets are implemented with a Linked List, the
    # time complexity of this function is O(n²)

    return "O(n)" or "O(n²)"
