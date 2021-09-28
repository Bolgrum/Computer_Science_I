# Homework 3.1                      VariedInputData.py
# Version:                          v2.0.7
# Completed by:                     Anthony Braden on 08/10/2021
from numpy import average

# 8.16 LAB: Varied amount of input data
# Statistics are often calculated with varying amounts of input 
# data. Write a program that takes any number of integers as 
# input, and outputs the average and max.
#
# Ex: If the input is:
#
# 15 20 0 5
# the output is:
#
# 10 20
# Note: For output, round the average to the nearest integer.

def gatherInput():
    print("Please input any number of integers below with a space separating individual numbers.")
    userInput = input("")
    return userInput

def generateTokens(userInput):
    tokens = userInput.split()
    
    inputData = []
    for token in tokens:
        inputData.append(int(token))
        
    return inputData
    
def findAverageValue(inputData):
    averageValue = sum(inputData) / len(inputData)
    return averageValue

def findMaxValue(inputData):
    maxValue = max(inputData)
    return maxValue

def printResults(averageValue, maxValue):
    print(f"The average value is: {averageValue:.0f}\nThe max value is: {maxValue}")
    
def runAgain():
    startAgain = input("Would you like to make another calculation? (Y/N)? > ")
    if(startAgain.lower() == "y"):
        runMain()
    elif(startAgain.lower() == "n"):
        print("Program closed.")
        exit()
    else:
        return runAgain()

def runMain():
    print("This program takes any number of integers as input and outputs the average and max values.")
    userInput = gatherInput()
    inputData = generateTokens(userInput)
    averageValue = findAverageValue(inputData)
    maxValue = findMaxValue(inputData)
    printResults(averageValue, maxValue)
    runAgain()
    
runMain()