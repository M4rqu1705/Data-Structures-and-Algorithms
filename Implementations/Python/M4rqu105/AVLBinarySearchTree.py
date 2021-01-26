#!/usr/bin/env python
# -*- coding: utf-8 -*-

class AVL_BST:
    class Node:
        def __init__(self, key = None):
            self.key = key
            self.left = None
            self.right = None

        def copy(self):
            newNode = AVL_BST.Node(self.key)
            newNode.left = self.left
            newNode.right = self.right
            return newNode

    def __init__(self):
        self.root = None
        self.current_size = 0


    def add(self, key):
        def aux(key, node):
            if node is None:
                return self.Node(key)

            elif key < node.key:
                node.left = aux(key, node.left)

            else:
                node.right = aux(key, node.right)

            return node

        self.root = aux(key, self.root)
        self.current_size += 1


    def remove(self, key):
        def aux(key, node):
            if key == node.key:

                if node.left is None and node.right is None:
                    del node
                    return None

                elif node.right is None:
                    node = node.left

                else:
                    left_most = node.right

                    while left_most.left is not None:
                        left_most = left_most.left

                    key = left_most.key
                    node.right = aux(key, node.right)
                    node.key = key


            elif key < node.key:
                node.left = aux(key, node.left)

            elif key > node.key:
                node.right = aux(key, node.right)

            return node

        self.root = aux(key, self.root)
        self.current_size -= 1


    def contains(self, key):
        def aux(key, node):
            if node is None:
                return False

            if key == node.key:
                return True

            elif key < node.key:
                return aux(key, node.left)

            elif key > node.key:
                return aux(key, node.right)

        return aux(key, self.root)


    def rebalance(self, node):

        def rotate_left(node):
            X = node.copy()
            Y = node.right.copy()

            X.right = Y.left
            Y.left = X

            return Y

        def rotate_right(node):
            X = node.copy()
            Y = node.left.copy()

            X.left = Y.right
            Y.right = X

            return Y

        def rotate_left_right(node):
            node.left = rotate_left(node.left)
            return rotate_right(node)

        def rotate_right_left(node):
            node.right = rotate_right(node.right)
            return rotate_left(node)



        if self.isBalanced(node):
            return node

        elif not self.isBalanced(node.right):
            if self.max_height(node.left) < self.max_height(node.right):
                # left-left
                return rotate_right(node)
            else:
                # left-right
                return rotate_left_right(node)

        else:
            if self.max_height(node.left) > self.max_height(node.right):
                # right-right
                return rotate_left(node)
            else:
                # right-left
                return rotate_right_left(node)


    def max_height(self, node=-1):
        if node == -1:
            node = self.root

        if node is None:
            return 0

        left_height = self.max_height(node.left)
        right_height = self.max_height(node.right)

        return max(left_height, right_height) + 1

    def min_height(self, node=-1):
        if node == -1:
            node = self.root

        if node is None:
            return 0

        left_height = self.min_height(node.left)
        right_height = self.min_height(node.right)

        return min(left_height, right_height) + 1

    def isBalanced(self, node=-1):
        if node == -1:
            node = self.root

        min_height = self.min_height(node)
        max_height = self.max_height(node)

        return min_height >= max_height - 1


    def size(self):
        return self.current_size

    def isEmpty(self):
        return self.size() == 0

    def clear(self):
        while not self.isEmpty():
            self.remove(self.root.key)

    def inorder(self, node = -1):
        if node == -1:
            node = self.root

        if node.left is not None:
            yield from self.inorder(node.left)

        yield node.key

        if node.right is not None:
            yield from self.inorder(node.right)

    def preorder(self, node = -1):
        if node == -1:
            node = self.root

        yield node.key

        if node.left is not None:
            yield from self.inorder(node.left)

        if node.right is not None:
            yield from self.inorder(node.right)

    def postorder(self, node = -1):
        if node == -1:
            node = self.root

        if node.left is not None:
            yield from self.inorder(node.left)

        if node.right is not None:
            yield from self.inorder(node.right)

        yield node.key

    def breadth_first(self, node = -1):
        if node == -1:
            node = self.root

        elif node is None:
            return []

        stack = [node]
        result = []

        while len(stack) > 0:
            node = stack.pop(0)

            result.append(node.key)

            if node.left is not None:
                stack.append(node.left)

            if node.right is not None:
                stack.append(node.right)

        return result

    def print_tree(self, node = -1, level=1):
        if node == -1:
            node = self.root

        if node != None:
            self.print_tree(node.right, level + 1)
            print(f'{"—"*(level - 1) * 4}→ [{node.key}]')
            self.print_tree(node.left, level + 1)



    def __str__(self):
        return ', '.join(list(self.inorder(self.root)))

    def __repr__(self):
        return str(self)



if __name__ == "__main__":
    bst = AVL_BST()

    bst.add(4)
    bst.add(2)
    bst.add(6)
    bst.add(1)
    bst.add(3)
    bst.add(1.5)
    bst.add(1.75)
    bst.add(5)
    bst.add(7)

    bst.print_tree()


    breakpoint()
