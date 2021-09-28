# Homework 2.1                      MadLib.py
# Version:                          v1.0.7
# Completed by:                     Anthony Braden on 08/03/2021

# 7.8 LAB: Mad Lib - loops
# Mad Libs are activities that have a person provide various words, which are then used to complete a short story in unexpected (and hopefully funny) ways.
#
# Write a program that takes a string and an integer as input, and outputs a sentence using the input values as shown in the example below. The program repeats until the input string is quit and disregards the integer input that follows.
#
# Ex: If the input is:
#
# apples 5
# shoes 2
# quit 0
# the output is:
#
# Eating 5 apples a day keeps the doctor away.
# Eating 2 shoes a day keeps the doctor away.

from gtts import gTTS
import os
import pygame

def chooseStory():
    print("Which story will you choose?")
    print("(1) Spooky Stuff\n(2) The News\n(3) A Letter from George")
    userInput = input(">")
    return userInput

def collectForStoryOne():
    adjective = input("Enter an adjective: > ")
    pluralNoun = input("Enter a plural noun: > ")
    pluralNoun2 = input("Enter a plural noun: > ")
    sillyWord = input("Enter a silly word: > ")
    liquid = input("Enter a liquid: > ")
    adjective2 = input("Enter an adjective: > ")
    noun = input("Enter a noun: > ")
    verb = input("Enter a verb: > ")
    pluralNoun3 = input("Enter a plural noun: > ")
    ing = input("Enter a verb ending in 'ing': > ")
    number = input("Enter a number: > ")
    ing2 = input("Enter a verb ending in 'ing': > ")
    pluralNoun4 = input("Enter a plural noun: > ")
    noun2 = input("Enter a noun: > ")
    print("Here we go!")
    
    madLib = (f"American children are fascinated by {adjective} stuff. Like stories that scare the {pluralNoun} off them or make their {pluralNoun2} stand on end.\n" +
     f"Scientists say this is because being frightened causes the {sillyWord} gland to function and puts {liquid} into their blood.\n" +
     f"And everyone knows that makes kids feel {adjective2}.\n" +
     f"When they are scared by a movie or a {noun}, boys laugh and holler and {verb}.\n" +
     f"But girls cover their eyes with their {pluralNoun3} and keep screaming and {ing}.\n" +
     f"Most kids get over this by the time they are {number} years old.\n" +
     f"Then they like movies about cars {ing2} or cops shooting {pluralNoun4}, or if they are girls, they like movies about a boy meeting a {noun2} and falling in love.\n" +
     f"Of course, that can be scary too.")
    
    return madLib
    
def collectForStoryTwo():
    noun = input("Enter a noun: > ")
    noun2 = input("Enter a noun: > ")
    pastVerb = input("Enter a past-tense verb: > ")
    noun3 = input("Enter a noun: > ")
    ing = input("Enter a verb ending in 'ing': > ")
    noun4 = input("Enter a noun: > ")
    verb = input("Enter a verb: > ")
    noun5 = input("Enter a noun: > ")
    bodyPart = input("Enter a body part: > ")
    adjective = input("Enter an adjective: > ")
    noun6 = input("Enter a noun: > ")
    verb2 = input("Enter a verb: > ")
    noun7 = input("Enter a noun: > ")
    pastVerb2 = input("Enter a past-tense verb: > ")
    month = input("Enter a month: > ")
    verb3 = input("Enter a verb: > ")
    noun7 = input("Enter a noun: > ")
    pastVerb3 = input("Enter a past-tense verb: > ")
    adjective2 = input("Enter an adjective: > ")
    verb4 = input("Enter a verb: > ")
    noun8 = input("Enter a noun: > ")
    pluralNoun = input("Enter a plural noun: > ")
    print("Here we go!")
    
    madLib = (f"A {noun} in a {noun2} was arrested this morning after he {pastVerb} in front of a {noun3}.\n" +
              f"He had a history {ing}, but no one -not even his {noun4}- ever imagined he'd {verb} with a {noun5} stuck in his {bodyPart}\n" +
              f"'I always thought he was {adjective}, but I never thought he'd do something like this'.\n" +
              f"Even his {noun6} was surprised!" +
              f"After a brief {verb2}, cops followed him to a {noun7}, where he reportedly {pastVerb2} in the fry machine.\n" +
              f"In {month}, a woman was charged with a similar crime, but rather than {verb3} with a {noun7}, she {pastVerb3} with a {adjective2} dog.\n" +
              f"Either way, we imagine after witnessing him {verb4} with a {noun8}, there are probably a whole lot of {pluralNoun} that are going to need some therapy.")
    
    return madLib

def collectForStoryThree():
    pluralNoun = input("Enter a plural noun: > ")
    occupation = input("Enter an occupation: > ")
    place = input("Enter the name of a place: > ")
    number = input("Enter a number: > ")
    adjective = input("Enter an adjective: > ")
    ing = input("Enter a verb ending in 'ing': > ")
    pluralNoun2 = input("Enter a plural noun: > ")
    place2 = input("Enter the name of a place: > ")
    adjective2 = input("Enter an adjective: > ")
    ing2 = input("Enter a verb ending in 'ing': > ")
    pluralNoun3 = input("Enter a plural noun: > ")
    adjective3 = input("Enter an adjective: > ")
    noun = input("Enter a noun: > ")
    bodyPart = input("Enter a body part: > ")
    verb = input("Enter a verb: > ")
    adjective4 = input("Enter an adjective: > ")
    bodyPart2 = input("Enter a body part: > ")
    print("Here we go!")
    
    madLib = (f"Hello, my fellow {pluralNoun} in twenty twenty-one, it's me, George Washington, the first {occupation}.\n" +
              f"I am writing from {place}, where I have been secretly living for the past {number} years.\n" +
              f"I am concerned by the {adjective} state of affairs in America these days.\n" +
              f"It seems that your politicians are more concerned with {ing} one another than with listening to the {pluralNoun2} of the people.\n" +
              f"When we declared our independence from {place2}, we set for on a {adjective2} path guided by the voices of the everyday {pluralNoun2}.\n" +
              f"If we're going to keep {ing2}, then we need to learn how to respect all {pluralNoun3}.\n" +
              f"Don't get me wrong; we had {adjective3} problems in my day too.\n" +
              f"Benjamin Franklin once called me a {noun} and kicked me in the {bodyPart}.\n" +
              f"But at the end of the day, we were able to {verb} in harmony.\n" + 
              f"Let us find that {adjective4} spirit once again, or else I'm taking my {bodyPart2} off the quarter!")
    
    return madLib
    
def playMusic():
    pygame.mixer.init()
    pygame.mixer.music.load("Itty Bitty.wav")
    pygame.mixer.music.play(-1)
    
def playStory(madLib):
    file = "MadLib.mp3"
    tts = gTTS(madLib)
    tts.save(file)
    os.system(file) 
    
def runMain():
    playMusic()
    storyChoice = chooseStory()
    if storyChoice == "1":
        madLib = collectForStoryOne()
    elif storyChoice == "2":
        madLib = collectForStoryTwo()
    elif storyChoice == "3":
        madLib = collectForStoryThree()
    else:
        return chooseStory()
    pygame.mixer.music.stop()
    playStory(madLib)
    
runMain()
    
    