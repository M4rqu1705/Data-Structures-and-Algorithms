#!/usr/bin/env python
# -*- coding: utf-8 -*-
import random
import time
import matplotlib.pyplot as plt
import numpy as np

from Sequential import SequentialFD
from SortedList import SortedListFD
from Ordered import OrderedFD
from Map import MapFD

def generate_random_data(size):
    data = []

    for i in range(size):
        data.append(random.randint(0, size // 2))

    return data


def run_tests():
    results = dict()

    X = []
    Y = [[], [], [], []]

    repetitions = 200
    start = 50
    end = 1000
    step = 50

    for i in range(start, end + step, step):
        temp_result = dict()
        data = generate_random_data(i)
        X.append(i)

        
        total_time = 0
        for j in range(repetitions):
            start_time = time.time()
            SequentialFD.computeFDList(data)
            total_time += time.time() - start_time

        temp_result['sequential'] = total_time / repetitions
        Y[0].append(temp_result['sequential'])


        total_time = 0
        for j in range(repetitions):
            start_time = time.time()
            SortedListFD.computeFDList(data)
            total_time += time.time() - start_time

        temp_result['sorted_list'] = total_time / repetitions
        Y[1].append(temp_result['sorted_list'])


        total_time = 0
        for j in range(repetitions):
            start_time = time.time()
            OrderedFD.computeFDList(data)
            total_time += time.time() - start_time
        temp_result['ordered'] = total_time / repetitions
        Y[2].append(temp_result['ordered'])


        total_time = 0
        for j in range(repetitions):
            start_time = time.time()
            MapFD.computeFDList(data)
            total_time += time.time() - start_time
        temp_result['map'] = total_time / repetitions
        Y[3].append(temp_result['map'])

        results[i] = temp_result

    X = np.array(X)
    Y[0] = np.array(Y[0])
    Y[1] = np.array(Y[1])
    Y[2] = np.array(Y[2])
    Y[3] = np.array(Y[3])

    plt.plot(X, Y[0], label='sequential')
    plt.plot(X, Y[1], label='sorted_list')
    plt.plot(X, Y[2], label='ordered')
    plt.plot(X, Y[3], label='map')

    plt.legend()
    plt.show()


if __name__ == "__main__":
    run_tests()
