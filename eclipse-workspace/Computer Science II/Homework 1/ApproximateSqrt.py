# Homework 1.1                      approximateSqrt.py
# Version:                          v1.0.0
# Completed by:                     Anthony Braden on 08/27/2021

# (Math: approximate the square root) There are several techniques 
# for implementing the sqrt function in the Math class. One such 
# technique is known as the Babylonian method. It approximates the 
# square root of a number, n, by repeatedly performing a calculation 
# using the following formula:
# 
# nextGuess = (lastGuess + n / lastGuess) / 2
# 
# When nextGuess and lastGuess are almost identical, nextGuess is the 
# approximated square root. The initial guess can be any positive value 
# (e.g., 1). This value will be the starting value for lastGuess. If 
# the difference between nextGuess and lastGuess is less than a very 
# small number, such as 0.0001, you can claim that nextGuess is the 
# approximated square root of n. If not, next-Guess becomes lastGuess 
# and the approximation process continues. 
# 
# Build a function to provide the square root of a number. 
# 
# Write another code to demonstrate your function works.

# Using a custom version of the program from:
# https://www.koderdojo.com/blog/python-program-square-roots-babylonian-method#:~:text=The%20Babylonian%20Method%20states%20that,divided%20by%20the%20previous%20guess.

import math
lastGuess = 1
epsilon = 0.000001

number = float(input("Calculate square root of? > "))

while True:
    difference = lastGuess**2 - number
    if abs(difference) <= epsilon:
        break
    nextGuess = (lastGuess + number / lastGuess) / 2.0
    lastGuess = nextGuess

print("Using math.sqrt(number) produces:", math.sqrt(number))
print("Using the Babylonian method produces", (nextGuess))
print("Difference between math.sqrt and the Babylonian method's guess:", (math.sqrt(number) - nextGuess))
    