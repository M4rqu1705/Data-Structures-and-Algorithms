#!/usr/bin/env python
# -*- coding: utf-8 -*-

from SinglyLinkedList import SinglyLinkedList
from BST import BinarySearchTree

class customBST(BinarySearchTree):
    # Part A
    def getPath(self, E, node = -1):
        # Consider some edge cases
        if node == -1:
            node = self.root
            
        # If the value is not found, the function returns null
        if not self.contains(E):
            return None

        # Begin to prepare results list
        result = SinglyLinkedList()

        result.append(node.key)

        if E < node.key:
            # Extend Singly linked list with deeper recursion's results
            result += self.getPath(E, node.left)

        elif E > node.key:
            # Extend Singly linked list with deeper recursion's results
            result += self.getPath(E, node.right)

        else:
            # If the value is found, end recursion and simply return the node's key
            return node.key

        return result

    
    # Part B
    def descendants(self, E, node=-1, parentFound = False):
        # Consider some edge cases ...
        if node == -1:
            node = self.root

        # If the value is not found, it returns null
        if not self.contains(E):
            return None

        if node is None:
            return None


        # Begin to prepare results list
        results = SinglyLinkedList()

        # Activate parentFound flag, meaning that we are ready to start adding data
        if node.key == E:
            parentFound = True

        # PERFORM PRE-ORDER TRAVERSAL

        # If key E was already found, append new stuff to results ...
        if parentFound:
            results = SinglyLinkedList()
            results.append(node.key)

        # Pass down results from deeper recursions
        left_results = self.descendants(E, node.left, parentFound)
        right_results = self.descendants(E, node.right, parentFound)

        if left_results is not None:
            results += left_results

        if right_results is not None:
            results += right_results

        return results


    # Part C
    def internalNodes(self, node = -1):
        # Consider some edge cases ...
        if node == -1:
            node = self.root

        # Begin to prepare results list
        results = SinglyLinkedList()

        # If we have any children
        if node.left is not None or node.right is not None:
            results.append(node.key)

        # Perform deeper recursions only where valid
        if node.left is not None:
            results += self.internalNodes(node.left)

        if node.right is not None:
            results += self.internalNodes(node.right)

        return results
