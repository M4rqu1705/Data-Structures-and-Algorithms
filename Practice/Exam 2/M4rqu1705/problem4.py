#!/usr/bin/env python
# -*- coding: utf-8 -*-

class ThreadedSinglyLinkedList:
    class Node:
        def __init__(self):
            self.data = None
            self.next = None
            self.thread = None

    def __init__(self):
        self.head = self.Node()
        self.tail = self.Node()
        self.threadHead = self.Node()
        self.currentSize = 0


    def threadCount(self):
        # Begin at the thread head and an initial counter value of 0
        current_node = self.threadHead
        counter = 0

        # Traverse the thread chain as long as possible, increasing the
        #  counter after visiting each node
        while current_node.thread is not None:
            current_node = current_node.thread
            counter += 1

        return counter

    # I'm not sure I understood it correctly
    def addToThread(self, obj):
        # Begin by finding the last element of the chain formed by the next references
        #
        # If the list were empty, 0 < 0 is false and the while loop will be skipped
        next_references_node = self.head
        i = 0
        while i < self.currentSize:
            next_references_node = next_references_node.next
            i += 1

        # Continue by getting to the beginning of the chain formed by the thread references
        #
        # If the list were empty, self.threadHead.thread is None and so this same exact None will be
        #  passed onto the newNode's thread pointer
        thread_references_node = self.threadHead

        # Finally, create and insert the newNode into the appropriate position
        newNode = self.Node()
        newNode.data = obj

        newNode.next = None
        next_references_node.next = newNode
        self.tail.next = newNode


        newNode.thread = thread_references_node.thread
        thread_references_node.thread = newNode

        # The list size is increased, so the currentSize should reflect that too
        self.currentSize += 1


    def eraseFromThread(self, obj):
        # Look for the first occurence of obj from the chain of thread references
        thread_references_node = self.threadHead

        # If the list were empty, self.threadHead.thread is None and the while loop will be skipped
        #
        # Otherwise, the while loop will only stop when the thread reference's value is the object we're looking for 
        while thread_references_node.thread is not None and thread_references_node.thread.data != obj:
            thread_references_node = thread_references_node.thread

        # Object was not found in the thread references
        if thread_references_node.thread is None:
            return False

        match = thread_references_node.thread

        
        # Look for the same element from the chain formed by the next references by using the python
        #  id() keyword. Its equivalent in C++ or Java would be to compare elements not by value,
        #  but checking if elements have the same pointers
        
        next_references_node = self.head
        i = 0
        while i < self.currentSize:
            # Same element was found!!!
            if id(next_references_node.next) == id(match) and next_references_node.next.data == match.data:
                break
            next_references_node = next_references_node.next
            i += 1

        
        # Reassign pointers to skip the match
        next_references_node.next = next_references_node.next.next
        thread_references_node.thread = thread_references_node.thread.thread

        del match
        # The list size is decreased, so the currentSize should reflect that too
        self.currentSize -= 1

        return True


    def print(self):
        next_references = []
        thread_references = []

        node = self.head
        i = 0
        while i < self.currentSize:
            next_references.append(node.next.data)
            node = node.next
            i += 1

        node = self.threadHead
        i = 0
        while i < self.threadCount():
            thread_references.append(node.thread.data)
            node = node.thread
            i += 1

        print(f"Next References: {', '.join(next_references)}")
        print(f"Thread References: {', '.join(thread_references)}")
