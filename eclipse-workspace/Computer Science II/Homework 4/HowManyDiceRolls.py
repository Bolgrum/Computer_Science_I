# Homework 5.2                      HowManyDiceRolls.py
# Version:                          v1.0.1
# Completed by:                     Anthony Braden on 09/24/2021

# 26.7 LAB: How many dice rolls?
# Given a GVDie object and an integer that represents the total 
# sum desired as parameters, complete function roll_total() that 
# returns the number of rolls needed to achieve at least the total 
# sum.
#
# Note: For testing purposes, the GVDie object is created in the 
# main() function using a pseudo-random number generator with a 
# fixed seed value. The program uses a seed value of 15 during 
# development, but when submitted, a different seed value will be 
# used for each test case. Refer to the textbook section on 
# random numbers to learn more about pseudo-random numbers.
#
# Ex: If the GVDie object is created with a seed value of 15 and 
# the input of the program is:
#
# 20
# the output is:
#
# Number of rolls to reach at least 20: 8

from GVDie import GVDie
import random

def rollTotal(die, total):
    totalValue = 0
    totalRolls = 0
    while totalValue < total:
        die.roll()
        totalValue += die.myValue
        totalRolls += 1
    return totalRolls 

def runAgain():
    startAgain = input("Would you like to perform another calculation? (Y/N)? > ")
    if(startAgain.lower() == "y"):
        runMain()
    elif(startAgain.lower() == "n"):
        print("Exiting program.")
        exit()
    else:
        return runAgain()
    
def runMain():
    die = GVDie()   
    die.setSeed(random.randint(1, 264))   
       
    try:          
        total = int(input('What total do you want to reach? > '))
        rolls = rollTotal(die, total) 
        print(f'Number of rolls to reach at least {total}: {rolls}')
    except ValueError:
        print('Please insert an integer.')
        return runMain()
    runAgain()
            
if __name__ == "__main__":
    runMain()
