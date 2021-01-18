#!/usr/bin/env python
# -*- coding: utf-8 -*-
from typing import Any, NoReturn

class BinarySearchTree:
    __slots__ = ['root', 'current_size']

    class Node:
        __slots__ = ['key', 'value', 'left', 'right']

        def __init__(self, key: Any = None, value: Any = None):
            self.key = key
            self.value = value
            self.left = None
            self.right = None

        def __str__(self):
            return f'{self.key}: {self.value}'

        def __repr__(self):
            return str(self)


    def __init__(self, key: Any, value: Any):
        self.root = self.Node(key, value)
        self.current_size = 1


    def get(self, key: Any, node=-1) -> Any:
        '''Get element with particular key

        Args:
            key: Key that is then matched with a value
            node: Node the search will start at

        Returns:
           any: Value of the element with the corresponding key

        Hint:
           Time complexity: O(log₂(n))

        '''
        def aux(key: Any, node) -> Any:
            if node is None:
                return None

            elif key == node.key:
                return node.value

            # If key is less than current node's key, get node from that subtree
            elif key < node.key:
                return aux(key, node.left)

            # If key is greater than to current node's key, get node from that subtree
            else:
                return aux(key, node.right)

        return aux(key, self.root)


    def add(self, key: Any, value: Any, node=-1) -> Any:
        '''Add element with specific keys

        Args:
           any: Key to be added
           any: Value to be added with key
           any: Node that will add key-value pair

        Returns:
           Node: Latest recursion's node

        Hint:
           Time complexity: O(log₂(n))

        '''

        def aux(key: Any, value: Any, node) -> Any:
            # If found empty spot, add new node there
            if node is None:
                self.current_size += 1
                return self.Node(key, value)

            # If key is less than current node's key, add new node to that subtree
            elif key < node.key:
                node.left = aux(key, value, node.left)

            # If key is greather than or equal to current node's key, add new node to that subtree
            else:
                node.right = aux(key, value, node.right)

            # By default return current node to update node in previous
            return node

        self.root = aux(key, value, self.root)


    def remove(self, key: Any, node=-1) -> Any:
        '''Remove element with particular key

        Args:
           any: Key with which we are looking for the value to be removed
           any: Node in which we are looking to remove value

        Returns:
           Node: Latest recursion's node

        Hint:
           Time complexity: O(log₂(n))
        '''

        def aux(key: Any, node) -> Any:
            if key < node.key:
                node.left = aux(key, node.left)

            elif key > node.key:
                node.right = aux(key, node.right)

            else:
                # If leaf node ...
                if node.left is None and node.right is None:
                    self.current_size -= 1
                    return None

                # If only has left node ...
                elif node.right is None:
                    self.current_size -= 1
                    # replace this node with the left node
                    return node.left

                # If has right node as well ...
                else:
                    left_most = node.right

                    while left_most.left is not None:
                        left_most = left_most.left

                    result = self.Node(left_most.key, left_most.value)
                    result.left = node.left
                    result.right = aux(left_most.key, node.right)
                    
                    # Replace current node with the leftmost
                    return result

            return node

        self.root = aux(key, self.root)


    def size(self) -> int:
        return self.current_size


    def isEmpty(self) -> bool:
        return self.size() == 0


    def contains(self, key: Any) -> bool:
        return self.get(key) is not None


    def clear(self) -> NoReturn:
        while not self.isEmpty():
            breakpoint()
            self.remove(self.root.key)


    def inorder(self, node = -1) -> Any:
        if node == -1:
            node = self.root

        if node.left is not None:
            yield from self.inorder(node.left)

        yield node

        if node.right is not None:
            yield from self.inorder(node.right)

    def preorder(self, node = -1) -> Any:
        if node == -1:
            node = self.root

        yield node

        if node.left is not None:
            yield from self.preorder(node.left)

        if node.right is not None:
            yield from self.preorder(node.right)


    def postorder(self, node = -1) -> Any:
        if node == -1:
            node = self.root

        if node.left is not None:
            yield from self.postorder(node.left)

        if node.right is not None:
            yield from self.postorder(node.right)

        yield node


    def __str__(self) -> str:
        if self.root is not None:
            return ', '.join([str(node) for node in self.inorder()])
        else:
            return ''


    def __repr__(self) -> str:
        return f'{{{str(self)}}}'


if __name__ == "__main__":
    bst = BinarySearchTree("Moe", 60)

    bst.add("Jil", 19)
    bst.add("Cal", 32)
    bst.add("Lydia", 30)
    bst.add("Kal-el", 17)
    bst.add("Ron", 19)
    bst.add("Owen", 40)
    bst.add("Xi", 29)

    print(list(bst.inorder()))
    print(list(bst.preorder()))
    print(list(bst.postorder()))

    breakpoint()


