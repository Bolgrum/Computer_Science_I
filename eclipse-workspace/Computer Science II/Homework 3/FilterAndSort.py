# Homework 3.1                      FilterAndSort.py
# Version:                          v2.0.6
# Completed by:                     Anthony Braden on 08/10/2021

# 8.17 LAB: Filter and sort a list
# Write a program that gets a list of integers from input, and 
# outputs non-negative integers in ascending order (lowest to 
# highest).
#
# Ex: If the input is:
#
# 10 -7 4 39 -6 12 2
# the output is:
#
# 2 4 10 12 39
# For coding simplicity, follow every output value by a space. 
# Do not end with newline.

def gatherInput():
    print("Please input any number of integers below with a space separating individual numbers.")
    userInput = input()
    return userInput

def generateTokens(userInput):
    tokens = userInput.split()
    
    inputData = []
    for token in tokens:
        if int(token) >= 0:
            inputData.append(int(token))

    return inputData

def sortData(inputData):
    inputData.sort()
    return inputData

def printResults(sortedData):
    for values in sortedData:
        print(values, end=' ')
    print("")
        
def runAgain():
    startAgain = input("Would you like to sort another integer list? (Y/N)? > ")
    if(startAgain.lower() == "y"):
        runMain()
    elif(startAgain.lower() == "n"):
        print("Program closed.")
        exit()
    else:
        return runAgain()
    
def runMain():
    print("This program outputs non-negative numbers in ascending order.")
    userInput = gatherInput()
    inputData = generateTokens(userInput)
    sortedData = sortData(inputData)
    printResults(sortedData)
    runAgain()
    
runMain()