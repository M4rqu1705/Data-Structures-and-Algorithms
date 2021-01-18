#!/usr/bin/env python
# -*- coding: utf-8 -*-

from FrequencyCounter import FrequencyCounter

from DoublyLinkedList import DoublyLinkedList

class SortedListFD(FrequencyCounter):

    def __init__(self):
        super("SortedList")

    @staticmethod
    def computeFDList(dataSet):
        # List of tuples
        results = DoublyLinkedList()

        for obj in dataSet:

            # Search results to see if obj is in the list. Stop when the next key is
            # greater than the current object
            found = False
            next_index = 0
            for i in range(len(results)):

                # If the element key is greater than the current object, there is no
                # need to keep iterating
                if results[i][0] > obj:
                    break
                else:
                    next_index = i+1

                # If it is found, add 1 to the counter
                if results[i][0] == obj:
                    results[i] = (results[i][0], results[i][1] + 1)
                    found = True
                    break


            # Insert element at the appropriate position when it was not found
            if not found:
                results.insert(next_index, (obj, 1))

        return results
