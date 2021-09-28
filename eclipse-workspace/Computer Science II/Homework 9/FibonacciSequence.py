# Homework 9.1                      FibonacciSequence.py
# Version:                          v2.0.5
# Completed by:                     Anthony Braden on 11/05/2021

# 14.7 LAB: Fibonacci sequence (recursion)
# The Fibonacci sequence begins with 0 and then 1 follows. All 
# subsequent values are the sum of the previous two, for example: 
# 0, 1, 1, 2, 3, 5, 8, 13. Complete the fibonacci() function, 
# which takes in an index, n, and returns the nth value in the 
# sequence. Any negative index values should return -1.
#
# Ex: If the input is:
#
# 7
# the output is:
# 
# fibonacci(7) is 13
# Note: Use recursion and DO NOT use any loops.

def fibonacciSequenceRecurser(n):
   if n <= 1:
       return n
   else:
       return(fibonacciSequenceRecurser(n-1) + fibonacciSequenceRecurser(n-2))

def getIndex():
    n = input("Please input a an index value to get started: > ")

    isInt = n.isdigit()
    if isInt == True:
        n = int(n)
        return n
    else:        
        print("\nYour value was not an integer.\nPlease enter an integer index value.\n")
        return getIndex()        
        
def generateFibonacciSequence(n):
    if int(n) <= 0:
        print("-1")
    else:
       print("Fibonacci sequence:")
       for i in range(int(n)):
           print("Term", str(i) + ":", fibonacciSequenceRecurser(i))
           
def runAgain():
    startAgain = input("Would you like to calculate another Fibonacci sequence (Y/N)? > ")
    if(startAgain.lower() == "y"):
        runMain()
    elif(startAgain.lower() == "n"):
        print("Thank you for using the Fibonacci Sequence Calculator.")
        exit()
    else:
        return runAgain()

def runMain():
    print("\nWelcome to the Fibonacci Sequence Calculator.")
    print("The Fibonacci sequence begins with 0 and then 1 follows.")
    print("All subsequent values are the sum of the two previous two,\nfor example: 0, 1, 1, 2, 3, 5, 8, 13.")
    nthTerm = getIndex()
    generateFibonacciSequence(nthTerm)
    runAgain()

runMain()
