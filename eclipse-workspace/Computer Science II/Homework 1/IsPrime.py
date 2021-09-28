# Homework 1.1                      IsPrime.py
# Version:                          v1.0.1
# Completed by:                     Anthony Braden on 08/27/2021

# (make an is prime function) Make a function for testing whether 
# a number is prime. Use this function to find the number of prime 
# numbers less than 10000.

def countPrimeNumbers(n):
    count = 0
    
    for num in range(n):
        if num <= 1:
            continue
        for i in range(2, num):
            if (num % i) == 0:
                break
        else:
            count += 1

    return count

print(countPrimeNumbers(10000))