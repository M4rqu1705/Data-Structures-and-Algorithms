#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Time complexity: O(n²), n = len(L)
def Replacer(L, X, Y):
    substitutions = 0

    while True:
        try:
            # Find index where X is first found
            index = L.index(X)

            # Remove first copy of X
            L.remove(X)
            # Insert element Y in the same position where the first copy of X previously was
            L.insert(index, Y)

            # Increase count after successful replacement
            substitutions += 1
        except:
            # Runs whenever `index = L.index(X)` results in an error
            break

    return substitutions

# Time complexity: O(n²*m² + k*n*m), n = len(theSets), m = average len of set in theSets, k = len(B)
def isPartition(theSets, B):
    # Helper set used to accumulate all sets and finally compare criteria 3
    accumulation = set()

    # O(n)
    for i in range(len(theSets)):

        # O(1)
        # Criteria 1: Set s_i is not empty
        if len(theSets[i]) == 0:
            return False

        # O(n*m * m) = O(n*m²)
        # Criteria 2: s_i and s_j do not have elements in common
        if len(accumulation.intersection(theSets[i])) != 0:
            return False

        # O(n*m * m) = O(n*m²)
        # Add all elements of s_i to accumulation
        accumulation = accumulation.union(theSets[i])

    #O(k * n*m)
    # Criteria 3: B = s_1 U s_2 U s_3 U ... U s_n
    # Return boolean to check if one is subset of another AND both sets have same length
    return B.issubset(accumulation) and len(B) == len(accumulation)



if __name__ == "__main__":
    L = ["Bob", "Joe", "Bob", "Ned", "Bob", "Ned"]
    print("Replacer:")
    print(Replacer(L, "Ned", "Jil"))
    print()
        
    theSets1 = [{"Joe"}, {"Ned"}, {"Amy", "Pol"}]
    B = {"Joe", "Ned", "Amy", "Pol"}
    theSets2 = [{"Joe", "Ned"}, {"Ned"}, {"Amy", "Pol"}]

    print("isPartition1:")
    print(isPartition(theSets1, B))
    print()

    print("isPartition2:")
    print(isPartition(theSets2, B))
    print()
