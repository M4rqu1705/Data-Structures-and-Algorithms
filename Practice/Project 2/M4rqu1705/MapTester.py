#!/usr/bin/env python
# -*- coding: utf-8 -*-

import config
import time
from Map import MapFD

class MapTester:

    @staticmethod
    def main():

        time_1 = 0.0
        time_2 = 0.0

        repetitions = config.repetitions

        with open('integerData.txt', 'r') as fp:
            data = fp.readlines()
            data = data.strip().lower().split(",")

            integers = map(lambda x: int(x), data)

            # Perform tests
            n = len(data)

            time_1 = time.time()
            for i in range(repetitions):
                MapFD.computeFDList(integers)

            time_1 = time.time() - time_1
            time_1 /= repetitions

            print(f'Integer test: {n} {time_1}')


        with open('stringData.txt', 'r') as fp:
            data = fp.readlines()
            data = data.strip().lower().split(",")

            strings = map(lambda x: int(x), data)

            # Perform tests
            n = len(data)

            time_2 = time.time()
            for i in range(repetitions):
                MapFD.computeFDList(strings)

            time_2 = time.time() - time_2
            time_2 /= repetitions

            print(f'String test: {n} {time_2}')


if __name__ == "__main__":
    MapTester.main()
