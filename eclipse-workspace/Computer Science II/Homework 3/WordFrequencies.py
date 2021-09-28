# Homework 3.3                      WordFrequencies.py
# Version:                          v1.0.0
# Completed by:                     Anthony Braden on 08/10/2021

# 25.13 LAB: Word frequencies (dictionaries)
#
# Implement the build_dictionary() function to build a word 
# frequency dictionary from a list of words.
#
# Ex: If the words list is:
#
# ["hey", "hi", "Mark", "hi", "mark"]
# the dictionary returned from calling build_dictionary(words) is:
#
# {'hey': 1, 'hi': 2, 'Mark': 1, 'mark': 1}
# Ex: If the words list is:
#
# ["zyBooks", "now", "zyBooks", "later", "zyBooks", "forever"]
# the dictionary returned from calling build_dictionary(words) is:
#
# {'zyBooks': 3, 'now': 1, 'later': 1, 'forever': 1}
# The main code builds the word list from an input string, 
# calls build_dictionary() to build the dictionary, and displays 
# the dictionary sorted by key value.

# The words parameter is a list of strings.
import pygame

def playMusic():
    pygame.mixer.init()
    pygame.mixer.music.load("Itty Bitty.wav")
    pygame.mixer.music.play(-1)
    
def chooseMusic():
    playMusic = input("Would you like to play music while you build your word frequency dictionary? (Y/N)? > ")
    if(startAgain.lower() == "y"):
        playMusic()
    elif(playMusic.lower() != "y" or playMusic.lower() != "n"):
        return runAgain()

def gatherInput():
    print("Please input a list of words with a space separating individual words.\nWords are case-sensitive.")
    userInput = input().lower()
    return userInput

def buildDictionary(words):
    
    frequencies = {}
    for word in words:
        if word in frequencies:
            frequencies[word] += 1
        else:
            frequencies[word] = 1
    return frequencies

def sortDictionaryKeys(dictionary):
    sortedKeys = sorted(dictionary.keys())
    return sortedKeys

def printResults(dictionary, sortedKeys):
    for key in sortedKeys:
        print(key + ': ' + str(dictionary[key]))
        
def runAgain():
    startAgain = input("Would you like to sort another build another word frequency dictionary? (Y/N)? > ")
    if(startAgain.lower() == "y"):
        runMain()
    elif(startAgain.lower() == "n"):
        print("Program closed.")
        exit()
    else:
        return runAgain()
        
def runMain():
    print("This program builds a word frequency dictionary from a list of words.")
    userInput = gatherInput()
    words = userInput.split()
    dictionary = buildDictionary(words)
    sortedKeys = sortDictionaryKeys(dictionary)
    printResults(dictionary, sortedKeys)
    runAgain()
    
if __name__ == '__main__':
    runMain()