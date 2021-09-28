# Homework 5.2                      ListExceptions.py
# Version:                          v1.0.1
# Completed by:                     Anthony Braden on 09/24/2021

# 10.9 LAB: Exceptions with lists
# Given a list of 10 names, complete the program that outputs the 
# name specified by the list index entered by the user. Use a try 
# block to output the name and an except block to catch any 
# IndexError. Output the message from the exception object if an 
# IndexError is caught. Output the first element in the list if 
# the invalid index is negative or the last element if the invalid 
# index is positive.
#
# Note: Python allows using a negative index to access a list, as long as the magnitude of the index is smaller than the size of the list.
#
# Ex: If the input of the program is:
#
# 5
# the program outputs:
#
# Name: Jane
# Ex: If the input of the program is:
#
# 12
# the program outputs:
#
# Exception! list index out of range
# The closest name is: Johnny
# Ex: If the input of the program is:
#
# -2
# the program outputs:
#
# Name: Tyrese
# Ex: If the input of the program is:
#
# -15
# the program outputs:
#
# Exception! list index out of range
# The closest name is: Ryley

import csv

def runMain():
    addLoadLookupList()
    runAgain()

def addLoadLookupList():
    names = []
    loadList(names)
    choice = input('Would you like to:\n1) Add to list\n2) Lookup from list\n> ')
    if choice == "1":
        addList(names)
    elif choice == "2":
        index = int(input('Please input an index value: > '))
        findName(names, index)
    else:
        return addLoadLookupList()
    
def addList(names):
    name = input('What name do you want to add? > ')
    with open('names.csv', 'a', newline='') as f:
        f.write('\n' + name)
    addLoadLookupList()

def loadList(names):
    with open('names.csv', newline='') as csvfile:
        reader = csv.reader(csvfile, delimiter=',')
        for name in reader:
            names.append(name)
    print(names)
    return names
        
def findName(names, index):
    try:
        print(f'Name: {names[index]}')
    except IndexError  as excpt:
        handleIndexException(names, index, excpt)
        
def handleIndexException(names, index, excpt):
    print(f'Exception! {excpt}')
    if index < 0:
        print(f'The closest name is: {names[0]}')
    else:
        print(f'The closest name is: {names[len(names) - 1]}')
        
def runAgain():
    startAgain = input("Would you like to look up another name in the list? (Y/N)? > ")
    if(startAgain.lower() == "y"):
        runMain()
    elif(startAgain.lower() == "n"):
        print("Exiting program.")
        exit()
    else:
        return runAgain()

if __name__ == '__main__':    
    runMain()