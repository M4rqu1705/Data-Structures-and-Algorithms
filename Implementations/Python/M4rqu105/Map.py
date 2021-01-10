#!/usr/bin/env python
# -*- coding: utf-8 -*-
from typing import Any, NoReturn

class Map:

    class Node:
        def __init__(self) -> NoReturn:
            self.key = None
            self.value = None
            self.next = None

    
    def __init__(self) -> NoReturn:
        self.head = self.Node()
        self.current_size = 0


    def get(self, key: Any) -> Any:
        if self.isEmpty():
            return None

        current_node = self.head

        while current_node.next.key != key and current_node.next.next is not None:
            current_node = current_node.next

        if current_node.next.key != key:
            return None
        else:
            return current_node.next.value


    def remove(self, key: Any) -> bool:
        if self.get(key) is None:
            return False

        current_node = self.head

        while current_node.next.key != key and current_node.next.next is not None:
            current_node = current_node.next

        temp = current_node.next
        current_node.next = current_node.next.next
        del temp

        self.current_size -= 1

        return True


    def put(self, key: Any, value: Any) -> bool:
        if value is None:
            return False

        if self.get(key) is not None:
            self.remove(key)

        new_node = self.Node()
        new_node.key = key
        new_node.value = value
        new_node.next = self.head.next
        self.head.next = new_node

        self.current_size += 1

        return True
   

    def containsKey(self, key: Any) -> bool:
        return self.get(key) is not None


    def getKeys(self):
        for key, value in self:
            yield key


    def getValues(self):
        for key, value in self:
            yield value


    def size(self) -> int:
        return self.current_size


    def isEmpty(self) -> bool:
        return self.size() == 0


    def clear(self) -> NoReturn:
        while self.head.next is not None:
            temp = self.head.next
            self.head.next = self.head.next.next
            del temp

        self.current_size = 0


    def __str__(self) -> str:
        message = []

        for key, value in self:
            message.append(''.join(["(", str(key), ", ", str(value), ")"]))

        return ', '.join(message)


    def __repr__(self) -> str:
        return str(self)


    def __iter__(self) -> Any:
        self.iteration_node = self.head.next
        return self

    def __next__(self):
        if self.iteration_node is not None:
            key, value = self.iteration_node.key, self.iteration_node.value
            self.iteration_node = self.iteration_node.next
            return (key, value)
        else:
            raise StopIteration





if __name__ == "__main__":
    m = Map()
    m.put("Sue", 14)
    m.put("Tom", 12)
    m.put("John", 10)
    m.put("Isabella", 10)
    m.put("John", 8)

    breakpoint()

