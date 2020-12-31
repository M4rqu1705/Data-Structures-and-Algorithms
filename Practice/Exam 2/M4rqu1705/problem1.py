def a():
    #
    # Final stack:
    #
    # "Xi"
    # "Jil"
    # "Joe"
    # ------------
    #
    return ["Joe", "Jil", "Xi"]

def b():
    #
    # Final stack:
    #
    # "Jil"
    # "Jil"
    # "Joe"
    # ------------
    #
    return ["Joe", "Jil", "Jil"]

def c():
    # 
    # The queue has a specific size which is decreased 1 by 1 with the dequeue operation.
    #
    # The while loop makes sure to run until the queue is empty. Therefore, it will run as
    #  many times as the size of the queue. If n = Q.size(), the time complexity is O(n)
    #
    return "O(n)"

def d():
    #
    # The first for loop iterates over the list L once. The second for loop iterates a constant
    #  "numSpaces * 2" amount of times and it seems like it does NOT depend on the list size.
    # 
    # If n = L.size(), the time complexity is O(n) since constants are removed from the Big-O
    #  notation
    #
    # ???----------------------------------------------------------------------------------???
    #
    # On the other hand, numSpaces is a variable the user will input and will affect the time
    #  complexity of the program. If n = L.size() and m = numSpaces, then the time complexity 
    #  would be O(n * m)
    #
    return "O(n)"

def e():
    #
    # The first for loop iterates over the list L once. The second for loop iterates 4 times (a
    #  constant amount)
    # 
    # If n = L.size(), the time complexity is O(n) since constants are removed from the Big-O
    #  notation
    #
    return "O(n)"


