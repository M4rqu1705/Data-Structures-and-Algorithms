#!/usr/bin/env python
# -*- coding: utf-8 -*-

from FrequencyCounter import FrequencyCounter

class MapFD(FrequencyCounter):

    def __init__(self):
        super("Map")

    @staticmethod
    def computeFDList(dataSet):
        results = []
        freq = dict()

        for el in dataSet:
            if freq.get(el, None) is None:
                freq[el] = 1
            else:
                freq[el] += 1

        for key in freq:
            results.append((key, freq[key]))

        return results
