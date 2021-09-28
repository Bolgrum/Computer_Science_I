# Homework 2.1                      Palindrome.py
# Version:                          v2.0.7
# Completed by:                     Anthony Braden on 08/03/2021

# 7.9 LAB: Palindrome
# 
# A palindrome is a word or a phrase that is the same when read 
# both forward and backward. Examples are: "bob," "sees," or 
# "never odd or even" (ignoring spaces). Write a program whose 
# input is a word or phrase, and that outputs whether the input 
# is a palindrome.
#
# Ex: If the input is:
#
# bob
# the output is:
#
# bob is a palindrome
# Ex: If the input is:
#
# bobby
# the output is:
#
# bobby is not a palindrome
# Hint: Start by removing spaces. Then check if a string is 
# equivalent to it's reverse.

import pygame
import time

def playMusic():
    pygame.mixer.init()
    pygame.mixer.music.load("Pixelland.wav")
    pygame.mixer.music.play(-1)
    
def gatherUserInput():
    userInput = input("Type in your word or phrase and see if it is a palindrome! > ")
    return userInput

def ignoreSpaces(userInput):
    originalStringWithoutSpaces = userInput.lower()
    originalStringWithoutSpaces = originalStringWithoutSpaces.replace(" ", "")
    return originalStringWithoutSpaces

def reverseString(originalString):
    reversedString = originalString[::-1]
    return reversedString

def calculateResult(originalString, reversedString, userInput):
    if originalString == reversedString:
        print(f'{userInput} is a palindrome!')
    else:
        print(f'{userInput} is not a palindrome...')
        
def runAgain():
    startAgain = input("Would you like to try another word? (Y/N)? > ")
    if(startAgain.lower() == "y"):
        runMain()
    elif(startAgain.lower() == "n"):
        print("Thank you for using the Palindrome Detector!")
        exit()
    else:
        return runAgain()

def runMain():
    playMusic()
    print("Welcome to the Palindrome Detector! A palindrome is a word \nor a phrase that is the same when read both forward and backward")
    userInput = gatherUserInput()
    originalString = ignoreSpaces(userInput)
    reversedString = reverseString(originalString)
    calculateResult(originalString, reversedString, userInput)
    runAgain()
    
runMain()