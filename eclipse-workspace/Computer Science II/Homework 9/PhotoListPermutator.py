# Homework 9.2                      PhotoListPermutator.py
# Version:                          v1.0.4
# Completed by:                     Anthony Braden on 11/05/2021

# 14.8 LAB: All permutations of names
# Write a program that lists all ways people can line up for a 
# photo (all permutations of a list of strings). The program 
# will read a list of one word names, then use a recursive 
# method to create and output all possible orderings of those 
# names, one ordering per line.
# 
# When the input is:
# 
# Julia Lucas Mia
# then the output is (must match the below ordering):
#
# Julia Lucas Mia
# Julia Mia Lucas
# Lucas Julia Mia
# Lucas Mia Julia
# Mia Julia Lucas
# Mia Lucas Julia

import itertools

listOfNames = []
           
def runMain():
    print("\nWelcome to the Photo List Permutator.")
    print("This program lists all the ways people can like up\nfor a photo.")
    print("Just enter in the names of everyone in your group\nand the program will do the rest.")
    
    count = 0
    
    numberOfUsers = obtainUserInput(count)
    permutateList(listOfNames, numberOfUsers)
    runAgain()
    
def obtainUserInput(count):
    name = input("Please enter a name or 'N' to stop > ")
    if name.lower() == "n":
        return count
    else:
        listOfNames.append(name)
        count += 1
        return obtainUserInput(count)

def permutateList(listOfNames, numberOfNames):
    permutatedList = list(itertools.permutations(listOfNames, numberOfNames))
    for item in permutatedList:
        print(item, end = ' ')
        print("")
    
def runAgain():
    startAgain = input("Would you like to calculate another list permutation (Y/N)? > ")
    if(startAgain.lower() == "y"):
        runMain()
    elif(startAgain.lower() == "n"):
        print("Thank you for using the Photo List Permutator.")
        exit()
    else:
        return runAgain()

runMain()