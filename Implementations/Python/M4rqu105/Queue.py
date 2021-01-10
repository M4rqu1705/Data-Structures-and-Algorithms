# -*- coding: utf-8 -*-
from typing import Any, NoReturn

DEFAULT_CAPACITY = 10

class Queue:
    '''FIFO (First-In Last-Out) Data Structure

    | Collection of elements with restriction on access. These are:
    |  - Elements are added at the end and removed from the front
    |  - There is no notion of specific position for elements other than element at the front. 
    |  - Repetitions are allowed

    | Implemented Queues with a circular array that gets expanded as needed

    Attributes:
       current_size(int): Stores how many elements are in the queue
       start(int): Index that points to the first element of the queue
       end(int): Index that points to the last element of the queue
       circular_array(list): Contains the circular array with the queue data

    '''

    def __init__(self, param: Any = None) -> NoReturn:
        '''Queue constructor

        Args:
           any: integer, Queue or iterator that is used to prepare the Queue's circular array.

        Raises:
           TypeError: Occurs when param is not an integer, iterator nor other Bag

        Example:
           >>> queue1 = Queue()
           >>> queue1
           []
           >>> queue2 = Queue([1,2,3])
           >>> queue2
           [1, 2, 3]
           >>> queue3 = Queue(queue2)
           >>> queue3
           [1, 2, 3]

        '''

        self.current_size = 0
        self.start = 0
        self.end = 0

        if isinstance(param, int):
            self.circular_array = [None] * param
        elif isinstance(param, Queue):
            original =  param.copy()

            self.circular_array = [None] * param.size()

            while not original.isEmpty():
                self.enqueue(original.dequeue())

        else:
            try:
                iter(param)

                self.circular_array = [None] * (len(param) + 1)

                for el in param:
                    self.enqueue(el)

            except TypeError:
                self.circular_array = [None] * DEFAULT_CAPACITY

            except:
                raise TypeError("invalid literal `param` for Queue constructor. Not an integer, iterator nor other Queue") from None


    def expand(self) -> NoReturn:
        '''Expand circular array capacity with which queue is implemented

        Duplicates the capacity of the circular array by making a new Queue,
        enqueueing all this queue's elements and copying all of the new queue's
        parameters to this one

        Hint:
           Time complexity: O(n)

        '''

        # Duplicate available storage
        newQueue = Queue(self.capacity() * 2)

        # Enqueue all of self's elements to newQueue
        while not self.isEmpty():
            newQueue.enqueue(self.dequeue())

        # Copy all attributes
        self.start = newQueue.start
        self.end = newQueue.end
        self.current_size = newQueue.size()
        self.circular_array = newQueue.circular_array[:]


    def enqueue(self, value: Any) -> bool:
        '''Appends element at the end of queue

        Besides appending to the end of the queue, it also checks if an expansion
        of the circular array is necessary

        Args:
           any: The value of the element that will be appended

        Returns:
           bool: True if operation was successful

        Example:
           >>> queue = Queue()
           >>> queue
           []
           >>> queue.enqueue(1)
           >>> queue
           [1]
           >>> queue.enqueue(6)
           >>> queue
           [1, 6]
           >>> queue.enqueue(3)
           >>> queue
           [1, 6, 3]
           >>> queue.enqueue(9)
           >>> queue
           [1, 6, 3, 9]

        Hint:
           | Average Time Complexity: O(1)
           | Worst-case Time Complexity: O(n)

        '''

        if self.capacity() - 1 == self.size():
            self.expand()

        # Set the value at the end position
        self.circular_array[self.end % self.capacity()] = value

        # Increase current_size counter
        self.current_size += 1

        # Since we appended to the end, we have to increase the end counter
        self.end = (self.start + self.size()) % self.capacity()

        return True


    def dequeue(self) -> True:
        '''Removes element from the front of queue

        Returns:
           bool: True if operation was successful

        Example:
           >>> queue = Queue([3, 2, 1])
           >>> queue
           [3, 2, 1]
           >>> queue.dequeue()
           >>> queue
           [2, 1]
           >>> queue.dequeue()
           >>> queue
           [1]
           >>> queue.dequeue()
           >>> queue
           []

        Hint:
           Time complexity: O(1)

        '''

        if self.isEmpty():
            return False

        # Extract value at start position
        value = self.circular_array[self.start % self.capacity()]

        # Nullify value at start position
        self.circular_array[self.start % self.capacity()] = None

        # Decrease current_size counter
        self.current_size -= 1

        # Since we removed from the front, we have to increase its counter
        self.start = (self.start + 1) % self.capacity()

        return value


    def front(self) -> Any:
        '''Previews element at front of queue without altering it

        Returns:
            any: Element at front of queue

        Example:
            >>> queue = Queue([3, 2, 1])
            >>> queue.front()
            3

        Hint:
            Time complexity: O(1)

        '''

        return self.circular_array[self.start % self.capacity()]


    def size(self) -> int:
        '''Returns amount of elements present in queue

        Returns:
            int: Size of queue

        Example:
            >>> queue = Queue([3, 2, 1])
            >>> queue.size()
            3

        Hint:
            Time complexity: O(1)

        '''

        return self.current_size


    def capacity(self) -> int:
        '''Returns amount of elements circular array is capable of holding

        As opposed to size/length, capacity establishes the maximum amount of
        elements container can hold

        Returns:
            int: Capacity of queue

        Example:
            >>> queue = Queue([3, 2, 1])
            >>> queue.capacity()
            10

        Hint:
            Time complexity: O(1)

        '''

        return len(self.circular_array)


    # Time complexity: O(1)
    def isEmpty(self) -> bool:
        '''Checks if the queue is empty

        Returns:
            bool: Returns true if the size of the queue is empty

        Example:
            >>> queue = Queue()
            >>> queue
            []
            >>> queue.isEmpty()
            True
            >>> queue = Queue([3, 2, 1])
            >>> queue
            [3, 2, 1]
            >>> queue.isEmpty()
            False

        Hint:
            Time complexity: O(1)

        '''
        return self.size() == 0


    # Time complexity: O(n)
    def clear(self) -> NoReturn:
        '''Removes all elements from queue

        It practically resets the queue to it's default state. However,
        it's previous capacity persists

        Example:
            >>> queue = Queue([3, 2, 1])
            >>> queue
            [3, 2, 1]
            >>> queue.clear()
            >>> queue
            []

        Hint:
            Time complexity: O(n)

        '''

        while not self.isEmpty():
            self.dequeue()

        self.start = 0
        self.end = 0
        self.current_size = 0


    # Time complexity: O(n)
    def copy(self) -> Any:
        '''Copies all of the queue's elements to a new queue without altering self

        Returns:
            Queue: copy of self's queue

        Hint:
            Time complexity: O(n)

        Example:
            >>> queue = Queue([3, 2, 1])
            >>> queue
            [3, 2, 1]
            >>> queue.copy()
            [3, 2, 1]
        '''
        tempQueue = Queue(self.capacity())
        copy = Queue(self.capacity())

        while not self.isEmpty():
            tempQueue.enqueue(self.front())
            copy.enqueue(self.dequeue())

        self.clear()

        while not tempQueue.isEmpty():
            self.enqueue(tempQueue.dequeue())

        return copy


    def __str__(self) -> str:
        '''Converts current queue to string

        Starts by making a copy and dequeueing all of it's elements to a list.
        The elements of the list are then joined by commas

        Returns:
            str: String representation of the queue

        Hint:
            Time complexity: O(n)
        '''
        copy = self.copy()

        elements = []

        while not copy.isEmpty():
            if copy.front() is not None:
                elements.append(copy.dequeue())
            else:
                copy.dequeue()

        return str(elements)


    def __repr__(self) -> str:
        '''Converts current queue to string

        Starts by making a copy and dequeueing all of it's elements to a list.
        The elements of the list are then joined by commas

        Returns:
            str: String representation of the queue

        Hint:
            Time complexity: O(n)
        '''
        return str(self)

    def __hash__(self) -> int:
        '''Generate a hash of this Queue using `FNV1A hash
        <https://en.wikipedia.org/wiki/Fowler%E2%80%93Noll%E2%80%93Vo_hash_function>`_

        Makes a copy of this Queue and uses FNV1A hash with a little tweak (I
        use modulo 1E19 just so numbers don't get TOO big)

        Returns:
            int: This Queue's hash code

        Hint:
            Time complexity: O(n)
        
        '''
        total = 2166136261
            
        copy = self.copy()

        while not copy.isEmpty():
            total *= 16777619
            total ^= hash(copy.dequeue())
            # A little extra just to prevent numbers from getting tooo big
            total % int(1E19)

        return total


if __name__ == "__main__":
    queue = Queue('Paco,Luis Daniel,Darlene,Zakira,Marcos,Sofía,Taimí,Maribel'.split(','))
    breakpoint()
