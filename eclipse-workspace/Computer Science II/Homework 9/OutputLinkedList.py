# Homework 9.3                      OutputLinkedList.py
# Version:                          v1.0.1.5
# Completed by:                     Anthony Braden on 11/05/2021

# 14.12 LAB: Output a linked list
# Write a recursive function called print_list() that outputs 
# the integer value of each node in a linked list. Function 
# print_list() has one parameter, the head node of a list. The 
# main program reads the size of the linked list, followed by 
# the values in the list. Assume the linked list has at least 1 
# node.
# 
# Ex: If the input of the program is:
# 
# 5
# 1
# 2
# 3
# 4
# 5
# the output of the print_list() function is:
# 
# 1, 2, 3, 4, 5,
# Hint: Output the value of the current node, then call the 
# print_list() function repeatedly until the end of the list is 
# reached. Refer to the Node class to explore any available 
# instance methods that can be used for implementing the 
# print_list() function.

class Node:
    def __init__(self, value):
        self.dataValue = value
        self.nextNode = None

    def insertAfter(self, node):
        tempNode = self.nextNode
        self.nextNode = node
        node.nextNode = tempNode

    def getNextNode(self):
        return self.nextNode

    def printData(self):
        print(self.dataValue, end=", ")

def printList(node):
    if node != None:
        node.printData()
        printList(node.getNextNode())
        
size = int(input())
value = int(input())
headNode = Node(value)
lastNode = headNode

for n in range(1, size):
    value = int(input())
    newNode = Node(value)
    lastNode.insertAfter(newNode)
    lastNode = newNode

printList(headNode)