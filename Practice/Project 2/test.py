import random
import time
import matplotlib.pyplot as plt
import numpy as np

def generate_random_data(size):
    data = []

    for i in range(size):
        data.append(random.randint(0, size // 2))

    return data

def sequential(data):
    # List of tuples
    results = []

    for obj in data:

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

def sorted_list(data):
    # List of tuples
    results = []

    for obj in data:

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

def ordered(data):
    data = sorted(data)

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

def Map(data):
    results = []
    freq = dict()

    for el in data:
        if freq.get(el, None) is None:
            freq[el] = 1
        else:
            freq[el] += 1

    for key in freq:
        results.append((key, freq[key]))

    return results



def real_one(data):
    freq = dict()

    for el in data:
        freq[el] = freq.get(el, 0) + 1

    return freq

def check(experiment, data):
    freq_experimental = experiment(data)
    freq = real_one(data)

    for el in freq_experimental:
        if el[1] != freq[el[0]]:
            print(f'Error!! {el} != {el[0]} -> {freq[el[0]]}')
            return None

    print(f'Success!')

def run_tests():
    results = dict()

    X = []
    Y = [[], [], [], []]

    repetitions = 1000
    for i in range(50, 1050, 50):
        temp_result = dict()
        data = generate_random_data(i)
        X.append(i)

        start_time = time.time()
        for j in range(repetitions):
            sequential(data)
        temp_result['sequential'] = (time.time() - start_time) / repetitions
        Y[0].append(temp_result['sequential'])

        start_time = time.time()
        for j in range(repetitions):
            sorted_list(data)
        temp_result['sorted_list'] = (time.time() - start_time) / repetitions
        Y[1].append(temp_result['sorted_list'])

        start_time = time.time()
        for j in range(repetitions):
            ordered(data)
        temp_result['ordered'] = (time.time() - start_time) / repetitions
        Y[2].append(temp_result['ordered'])

        start_time = time.time()
        for j in range(repetitions):
            Map(data)
        temp_result['map'] = (time.time() - start_time) / repetitions
        Y[3].append(temp_result['map'])

        results[i] = temp_result

    #  print(results)

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


#  data = generate_random_data(100)
#  check(sequential, data)
#  check(sorted_list, data)
#  check(ordered, data)
#  check(Map, data)

run_tests()
                
