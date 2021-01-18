#!/usr/bin/env python
# -*- coding: utf-8 -*-

from FrequencyCounter import FrequencyCounter

class SequentialFD(FrequencyCounter):

    def __init__(self):
        super("Sequential")

    @staticmethod
    def computeFDList(dataSet):
        # List of tuples
        results = []

        for obj in dataSet:

            # Search results to see if obj is in the list
            found = False
            for i in range(len(results)):
                el = results[i]

                # If it is found, add 1 to the counter
                if el[0] == obj:
                    results[i] = (results[i][0], results[i][1] + 1)
                    found = True
                    break

            # Add new element at the end when it was not found
            if not found:
                results.append((obj, 1))

        return results
