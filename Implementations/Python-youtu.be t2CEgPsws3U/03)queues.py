#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Queue functions: enqueue, dequeue, front, size
# Queues are "First In, First Out" (FIFO)

class Queue:
    def __init__(self):
        self.queue = []

    def enqueue(self, el):
        self.queue.append(el)

    def dequeue(self):
        if self.size() > 0:
            return self.queue.pop(0)
        else:
            return None

    def front(self):
        if self.size() > 0:
            return self.queue[0]
        else:
            return None

    def size(self):
        return len(self.queue)

# Priority Queues are the same as queues, except elements they enqueue have a set priority
# Elements with priority 1 have greater priority than elements with priority 2 or 3
# If every element has same priority, it's just a normal queue

class PriorityQueue(Queue):
    def enqueue(self, el, priority = 5):
        if self.size() == 0:
            self.queue.append((el, priority))

        else:
            # Append at begining, if it meets criteria
            for i in reversed(range(self.size())):
                if priority < self.queue[i][1]:
                    self.queue.insert(i, (el, priority))
                    return

            self.queue.append((el, priority))

    def dequeue(self):
        return super().dequeue()[0]

    def front(self):
        return super().front()[0]


def queue_test():
    line = Queue()

    line.enqueue(1)
    line.enqueue(2)
    line.enqueue(3)
    line.enqueue(4)

    while line.size() > 0:
        print(line.dequeue())


def priority_queue_test():
    line = PriorityQueue()

    line.enqueue(1, 1)
    line.enqueue(2, 4)
    line.enqueue(3, 2)
    line.enqueue(4, 3)

    print(line.queue)

    while line.size() > 0:
        print(line.dequeue())


def main():
    queue_test()
    priority_queue_test()


if __name__ == "__main__":
    main()

