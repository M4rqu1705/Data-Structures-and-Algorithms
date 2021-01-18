#!/usr/bin/env python
# -*- coding: utf-8 -*-

from FrequencyCounter import FrequencyCounter

class OrderedFD(FrequencyCounter):

    def __init__(self):
        super("Ordered")

    @staticmethod
    def computeFDList(dataSet):
        data = sorted(dataSet)

        # List of tuples
        results = []

        i = 0
        while i < len(data):

            obj = data[i]
            count = 0
            while i < len(data) and data[i] == obj:
                count += 1
                i += 1
            
            results.append((obj, count))

        return results
