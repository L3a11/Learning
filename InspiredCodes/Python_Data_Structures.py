# This repository contains code snippets and examples for Data Structures and Algorithms written in Python and HTML. These examples are intended to be used as a reference for developer students for inspiration and learning.

# Data Structures

# 1. Linked List

class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return
        last_node = self.head
        while last_node.next:
            last_node = last_node.next
        last_node.next = new_node

# This example of a linked list data structure is good for storing and managing a collection of elements that need to be accessed and manipulated sequentially. Linked lists are particularly useful when insertion and deletion of elements frequently occur, as they can easily accommodate changes in size without needing to resize memory allocation. 

# 2. Stack

class Stack:
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if not self.is_empty():
            return self.items.pop()

    def peek(self):
        if not self.is_empty():
            return self.items[-1]

    def is_empty(self):
        return len(self.items) == 0

# This example of a stack data structure is good for implementing algorithms that require last-in, first-out (LIFO) behavior. Stacks are commonly used in programming for tasks such as reversing a list, evaluating arithmetic expressions, and backtracking in algorithms. This implementation of a stack allows for adding and removing items, checking the top item without removing it, and checking if the stack is empty.

