#!/usr/bin/env python
# -*- coding: utf-8 -*-

from StackQueue import Stack, Queue

def deleteFromStack(stack, obj):

    helper = Stack()

    # Transfer all contents of the StaticArrayStack to another helper stack
    while not stack.isEmpty():
        helper.push(stack.pop())

    # Transfer all the contents of the helper stack to the StaticArrayStack 
    #  while filtering for objects we want to delete
    while not helper.isEmpty():
        if obj != helper.top():
            stack.push(helper.pop())
        else:
            helper.pop()

    return stack


def deleteFromQueue(queue, obj):

    helper = Queue()

    # Transfer all contents of the main Queue to another helper queue
    while not queue.isEmpty():
        helper.enqueue(queue.dequeue())

    # Transfer all the contents of the helper queue to the main Queue 
    #  while filtering for objects we want to delete
    while not helper.isEmpty():
        if obj != helper.front():
            queue.enqueue(helper.dequeue())
        else:
            helper.dequeue()

    return queue


def copyQueue(src):

    copy = Queue()

    # Simply dequeue each element of the src queue and instantaneously enqueue back to the src and
    #  to the copy. Do this a src.size() amount of times (for every element in the src queue)
    for i in range(src.size()):
        value = src.dequeue()

        copy.enqueue(value)
        src.enqueue(value)

    return copy
