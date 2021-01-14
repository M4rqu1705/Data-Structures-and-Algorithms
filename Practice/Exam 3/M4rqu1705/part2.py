#!/usr/bin/env python
# -*- coding: utf-8 -*-
from HashMaps import SeparateChaining, OpenAddressing


def a():
    # Assuming that the sub-lists are each one of the buckets, implemented as a
    # Doubly-Linked List, and repeated hashes are inserted at the end of the
    # bucket:

    return [
            [],
            [21, 11, 1],
            [22],
            [3],
            [94],
            [25],
            [56],
            [17],
            [78],
            [9],
            ]


# Part B
class customSeparateChaining(SeparateChaining):
    def bucketPals(self, obj):
        # If the element obj is not found in the hash table, the method returns null
        if self.get(obj) is None:
            return None

        # In Java:
        # int position =  hashFunction.hashCode(obj) % self.buckets.length
        position = hash(obj) % self.amount_buckets()

        # Search for all the elements inside the buckets ...
        elements = []

        bucket = self.buckets[position]

        while bucket.next is not None:
            # Append as tuple fo key-value pairs
            elements.append((bucket.next.key, bucket.next.value))
            bucket = bucket.next

        return elements


# Part C
class customOpenAddressing(OpenAddressing):
    def collisionDistance(self, obj) -> int:

        #  The function returns -1 if obj is not in the hash table
        if self.get(obj) is None:
            return -1

        proper_bucket = hash(obj) % self.capacity()

        # The function returns 0 if the element obj is in the bucket that the
        # hash function specifies (proper bucket)

        if self.buckets[proper_bucket].key == obj:
            return 0

        else:
            # Linear probe within the buckets to find collision distance

            distance = 1

            while self.buckets[(proper_bucket + distance) % self.capacity()].key != obj:
                distance += 1

            return distance
