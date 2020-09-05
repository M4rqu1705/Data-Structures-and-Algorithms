#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Binary Search Tree functions: add, findMin
# Helps searching for element in log(n) time

class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

class BinarySearchTree:
    def __init__(self):
        self.root = None

    def add(self, data):
        if self.root == None:
            self.root = Node(data)
            return
        else:

            def searchTree(node):
                if data > node.data and node.right is None:
                    node.right = Node(data)
                elif data > node.data and node.right is not None:
                    searchTree(node.right)
                elif data < node.data and node.left is None:
                    node.left = Node(data)
                elif data < node.data and node.left is not None:
                    searchTree(node.left)

            searchTree(self.root)

    def findMin(self, node=None):
        if node == None:
            node = self.root

        while isinstance(node.left, Node):
            node = node.left

        return node.data

    def findMax(self, node=None):
        if node == None:
            node = self.root

        while isinstance(node.right, Node):
            node = node.right

        return node.data

    def find(self, data, node=None):
        if node == None:
            node = self.root

        if isinstance(node, Node):
            if data > node.data:
                return self.find(data, node.right)
            elif data < node.data:
                return self.find(data, node.left)
            else:
                return node
        else:
            return None
             

def bst_test():
    bst = BinarySearchTree()

    bst.add(50)
    bst.add(17)
    bst.add(72)
    bst.add(12)
    bst.add(23)
    bst.add(54)
    bst.add(76)
    bst.add(9)
    bst.add(14)
    bst.add(19)
    bst.add(67)

    print(bst.findMin())
    print(bst.findMax())
    #  print(bst.find(76))


def main():
    bst_test()


if __name__ == "__main__":
    main()

