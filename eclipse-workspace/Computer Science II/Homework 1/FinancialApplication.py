# Homework 1.1                      FinancialApplication.py
# Version:                          v1.1.6
# Completed by:                     Anthony Braden on 08/27/2021

# (Financial application: compute the future investment value) Write a function 
# that computes future investment value at a given interest rate for a specified number of years.
#
# For example, calculateFutureInvestmentValue(10000, 0.05/12, 5) returns 12833.59.
#
# Write a test program that prompts the user to enter the investment amount (e.g.,
# 1000) and the interest rate (e.g., 9%) and prints a table that displays future value
# for the years from 1 to 30.
    
from tabulate import tabulate
    
def runMain():

    futureValues = [[], []]
    
    printIntro()
    fillFutureValuesTable(futureValues)
    printResults(futureValues)
    print("")
    
    runAgain()

def printIntro():
    print("\nWelcome to the Future Investment Calculator\n")    
    print("Time Value of Money Consideration\r")
    print("Understanding the time value of money and the exponential growth created by\ncompounding is essential for investors looking to optimize their income and\nwealth allocation.\r")
    print("The formula for obtaining the future value (FV) and present value (PV) are as\nfollows:\r\nFV = PV(1 + i)^n\r")

def fillFutureValuesTable(futureValues):
    initialInvestmentValue = input("What is your initial investment value? > $")
    interestRate = input("What is your annual interest rate? > ")
    years = input("How many years? > ")
    print("")  
    
    for i in range(int(years)+1):
        nestedFutureYears = futureValues[0]
        nestedFutureYears.append('Year ' + str(i))
        
    for i in range(len(futureValues[0])):
        nestedFutureValues = futureValues[1]
        currentFutureValue = calculateFutureInvestmentValue(initialInvestmentValue, interestRate, i)
        nestedFutureValues.append(currentFutureValue)
                    
def calculateFutureInvestmentValue(initialInvestmentValue, interestRate, i):
    futureValue = round(float(initialInvestmentValue) * (1 + float(interestRate)) ** float(i), 2)
    return futureValue    

def printResults(futureValues):
    print(tabulate(futureValues, headers="firstrow", floatfmt='.2f', tablefmt='grid'))

def runAgain():
    startAgain = input("Would you like to calculate another investment (Y/N)? > ")
    if(startAgain.lower() == "y"):
        runMain()
    elif(startAgain.lower() == "n"):
        print("Thank you for using the Future Investment Calculator.")
        exit()
    else:
        return runAgain()
        
runMain()