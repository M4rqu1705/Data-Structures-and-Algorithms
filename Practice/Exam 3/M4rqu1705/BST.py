#!/usr/bin/env python
# -*- coding: utf-8 -*-
from typing import Any, NoReturn

class BinarySearchTree:
    class BSTNode:
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
        self.root = self.BSTNode(key, value)
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
        if node == -1:
            node = self.root

        if node is None:
            return None

        elif node.key == key:
            return node.value

        elif key < node.key:
            return self.get(key, node.left)

        else:
            return self.get(key, node.right)

    
    def add(self, key: Any, value: Any, node=-1) -> bool:
        '''Add element with specific keys

        Args:
           any: Key to be added
           any: Value to be added with key
           any: Node that will add key-value pair

        Returns:
           bool: True if operation is successful
        
        Hint:
           Time complexity: O(log₂(n))

        '''

        if node == -1:
            node = self.root

        if self.root is None:
            self.root = self.BSTNode(key, value)
            return True

        else:
            # Check if can be added to the left
            if key < node.key:
                if node.left is None:
                    node.left = self.BSTNode(key, value)
                    self.current_size += 1
                else:
                    self.add(key, value, node.left)

            # Check if can be added to the right
            elif key > node.key:
                if node.right is None:
                    node.right = self.BSTNode(key, value)
                    self.current_size += 1
                else:
                    self.add(key, value, node.right)

            # Replace current node's value with the new one
            else:
                node.value = value

            return True

    
    def remove(self, key: Any, node=-1) -> bool:
        '''Remove element with particular key

        Args:
           any: Key with which we are looking for the value to be removed
           any: Node in which we are looking to remove value

        Returns:
           bool: True if operation is successful

        Hint:
           Time complexity: O(log₂(n))
        '''

        if node == -1:
            node = self.root

        if node is None:
            return False

        if self.get(key) is None:
            return False

        if self.root.key == key and self.root.left is None and self.root.right is None:
            self.root = None
            self.current_size -= 1

        elif key < node.key:

            # Edge case for leaf nodes
            if node.left.key == key and node.left.left is None and node.left.right is None:
                node.left = None
                self.current_size -= 1
                return True

            # Every other case
            else:
                return self.remove(key, node.left)


        elif key > node.key:

            # Edge case for leaf nodes
            if node.right.key == key and node.right.left is None and node.right.right is None:
                node.right = None
                self.current_size -= 1
                return True

            # Every other case
            else:
                return self.remove(key, node.right)

        else:
            # If is a leaf node
            if node.left is None and node.right is None:
                return True

            # If is internal node with no right child
            elif node.right is None:
                node.key = node.left.key
                node.value = node.left.value
                node.right = node.left.right
                node.left = node.left.left

                self.current_size -= 1

                return True

            # If is internal node with children
            else:
                # Go to leftmost node on right subtree
                left_most = node.right
                parent = node
                while left_most.left is not None:
                    parent = left_most
                    left_most = left_most.left

                # Replace with that left-most node
                node.key = left_most.key
                node.value = left_most.value
                
                # Delete left-most node from tree
                if left_most is node.right:
                    parent.right = None
                else:
                    parent.left = None

                self.current_size -= 1
                
                return True


    def size(self) -> int:
        return self.current_size
    

    def isEmpty(self) -> bool:
        return self.size() == 0


    def contains(self, key: Any) -> bool:
        return self.get(key) is not None


    def clear(self):
        while not self.isEmpty():
            self.remove(self.root.key)


    def inorder(self, node = -1):
        if node == -1:
            node = self.root

        if node.left is not None:
            yield from self.inorder(node.left)

        yield node

        if node.right is not None:
            yield from self.inorder(node.right)

    def preorder(self, node = -1):
        if node == -1:
            node = self.root

        yield node

        if node.left is not None:
            yield from self.preorder(node.left)

        if node.right is not None:
            yield from self.preorder(node.right)


    def postorder(self, node = -1):
        if node == -1:
            node = self.root

        if node.left is not None:
            yield from self.postorder(node.left)

        if node.right is not None:
            yield from self.postorder(node.right)

        yield node


    def __str__(self):
        if self.root is not None:
            return ', '.join([str(node) for node in self.inorder()])
        else:
            return ''


    def __repr__(self):
        return f'{{{str(self)}}}'


if __name__ == "__main__":
    bst = BinarySearchTree("Moe", ("Moe", 24, "NY"))

    bst.add("Jil", ("Jil", 19, "SF"))
    bst.add("Cal", ("Cal", 32, "LA"))
    bst.add("Lydia", ("Lydia", 30, "NM"))
    bst.add("Kal-el", ("Kal-el", 17, "Smallville"))
    bst.add("Ron", ("Ron", 19, "LA"))
    bst.add("Owen", ("Owen", 40, "CH"))
    bst.add("Xi", ("Xi", 29, "SJ"))

    print(bst.remove("Xi"))
    print(bst)
