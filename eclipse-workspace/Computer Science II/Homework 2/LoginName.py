# Homework 2.1                      LoginName.py
# Version:                          v1.0.5
# Completed by:                     Anthony Braden on 08/03/2021

# 24.9 LAB: Login name
#
# Write a program that creates a login name for a user, given 
# the user's first name, last name, and a four-digit integer as 
# input. Output the login name, which is made up of the first 
# five letters of the last name, followed by the first letter of 
# the first name, and then the last two digits of the number 
# (use the % operator). If the last name has less than five 
# letters, then use all letters of the last name.
#
# Ex: If the input is:
#
# Michael Jordan 1991
# the output is:
#
# Your login name: JordaM91
# Ex: If the input is:
#
# Kanye West 2024
# the output is:
#
# Your login name: WestK24
import time

def gatherUserInput():
    userInput = input("Please input your first name, last name, and birth year\nin order to generate your user ID (Ex. John Doe 1992) > ")
    return userInput

def generateUserName(userInput):
    tokens = userInput.split(" ")
    first = tokens[0]
    last = tokens[1]
    year = int(tokens[2])
    
    if len(last) > 5:
       last = last[:5]
        
    output = (f"Your user name: {last}{first[0]}{year % 100}")
    return output

def printGoofyStuff():
    print("Collecting tokens...")
    time.sleep(2)
    print("Cutting and pasting...")
    time.sleep(2)
    print("Generating user name in:")
    time.sleep(2)
    print("3...")
    time.sleep(1)
    print("2...")
    time.sleep(1)
    print("1...")
    time.sleep(1)
    print("Ding!\n")
    time.sleep(1)    

def runAgain():
    startAgain = input("Would you like to generate another user name? (Y/N)? > ")
    if(startAgain.lower() == "y"):
        runMain()
    elif(startAgain.lower() == "n"):
        print("Bye bye!")
        exit()
    else:
        return runAgain()
        
def runMain():
    userInput = gatherUserInput()
    output = generateUserName(userInput)
    printGoofyStuff()
    print(output + "\n")
    runAgain()
    
runMain()