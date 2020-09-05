#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Stack functions: push, pop, peek, length
# Stacks are "Last In, First Out" (LIFO)
class Stack:
    def __init__(self):
        self.stack = []

    def push(self, el):
        self.stack.append(el)

    def pop(self):
        if self.length() > 0:
            return self.stack.pop()
        else:
            return None

    def peek(self):
        if self.length() > 0:
            return self.stack[-1]
        else:
            return None

    def length(self):
        return len(self.stack)


def balanced_parens(expression):
    #1) Check if the following expression has balanced characters

    matching = {
            "(": ")",
            "[": "]",
            "{": "}",
            "<": ">",
            '"': '"',
            "'": "'",
            "`": "`",
            }

    stack = Stack()

    for character in expression:

        # If character is matching the character to last element in stack
        if character == matching.get(stack.peek()):
            stack.pop()

        # The character is inside the matching keys ...
        elif matching.get(character) is not None:
            # Push it into stack
            stack.push(character)

    if stack.length() == 0:
        return True
    else:
        return False


def reverse_string(string):
    stack = Stack()

    reversed_string = ""

    for char in string:
        stack.push(char)

    for i in range(stack.length()):
        reversed_string += stack.pop()

    return reversed_string


def prefix_notation(expression):
    operands = Stack()

    operators = {"+", "-", "*", "/", "^"}
    ignore = {" "}

    output = ""

    for el in expression:
        if el not in operators and el not in ignore:
            operands.push(el)

        elif el in operators:
            if operands.length() > 0:
                operand = operands.pop()
                output += el + operand

    return output + operands.pop()



def main():
    # There is no need to implement stack class since Python arrays serve as stacks themselves

    print(balanced_parens("({[Wenas](Adios)''``()})"))

    print(reverse_string("a man a plan a canal panama"))

    print(prefix_notation("a + b - c"))




if __name__ == "__main__":
    main()

