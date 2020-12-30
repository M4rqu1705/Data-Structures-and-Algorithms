from DoublyLinkedList import DoublyLinkedList

# These are last-minute Stack and Queue implementations I am making to prepare for
#  the second test

class Stack:
    def __init__(self):
        self.stack = DoublyLinkedList()

    def push(self, el):
        self.stack.insert(0, el)

    def pop(self):
        value = self.stack[0]
        self.stack.delete(0)
        return value

    def top(self):
        return self.stack[0]

    def size(self):
        return self.stack.size()

    def isEmpty(self):
        return self.size() == 0

    def clear(self):
        self.stack.clear()

    def __len__(self):
        return self.size()


class Queue:
    def __init__(self):
        self.queue = DoublyLinkedList()

    def enqueue(self, el):
        self.queue.append(el)

    def dequeue(self):
        value = self.queue[0]
        self.queue.delete(0)
        return value

    def front(self):
        return self.queue[0]

    def size(self):
        return self.queue.size()

    def isEmpty(self):
        return self.size() == 0

    def clear(self):
        self.queue.clear()

    def __len__(self):
        return self.size()
