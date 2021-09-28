# Homework 5.3                      RollingAPair.py
# Version:                          v1.0.1
# Completed by:                     Anthony Braden on 09/24/2021

# 26.16 LAB: Rolling for a pair
# Given two GVDie objects that represent 2 six-sided dice and an 
# integer that represents a desired value as parameters, complete 
# the function rolling_for_pair(). The function rolling_for_pair() 
# rolls the dice until a pair with the desired value is rolled and 
# then returns the number of rolls thrown to achieve the result. 
# Assume the desired value received from input is within the 
# appropriate range, 1-6.
#
# Note: For testing purposes, the GVDie objects are created in the 
# main() function using a pseudo-random number generator with a 
# fixed seed value. The program uses a seed value of 15 during 
# development, but when submitted, a different seed value will be 
# used for each test case. Refer to the textbook section on 
# random numbers to learn more about pseudo-random numbers.
#
# Ex: If the GVDie objects are created with a seed value of 15 and 
# the input of the program is:
#
# 3
# the output is:
#
# It took 13 rolls to get a pair of 3's.

from GVDie import GVDie
import random

def rollDice():
    die1 = GVDie()   
    die2 = GVDie()   
    die1.setSeed(random.randint(1, 264))
    die2.setSeed(random.randint(1, 264))
          
    value = int(input("What integer would you like to roll? (1-6)> "))
    if value <= 6:
        rolls = rollingForPair(die1, die2, value)
        if rolls == "1": 
            print(f'It took {rolls} roll to get a pair of {value}\'s.')
        else:
            print(f'It took {rolls} rolls to get a pair of {value}\'s.')
    else:    
        return runMain()    

def rollingForPair(d1, d2, val):
    d1.roll()
    d2.roll()
    rolls = 1
    while d1.myValue != val or d2.myValue != val:
        d1.roll()
        d2.roll()
        rolls += 1  
    return rolls 

def runAgain():
    startAgain = input("Would you like to roll for another pair? (Y/N)? > ")
    if(startAgain.lower() == "y"):
        runMain()
    elif(startAgain.lower() == "n"):
        print("Bye bye!")
        exit()
    else:
        return runAgain()
    
def runMain():
    rollDice()
    runAgain()

if __name__ == "__main__":
    runMain()
