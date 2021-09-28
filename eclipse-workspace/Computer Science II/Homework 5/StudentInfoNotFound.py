# Homework 5.3                      StudentInfoNotFound.py
# Version:                          v2.0.6
# Completed by:                     Anthony Braden on 09/24/2021

# 10.12 LAB: Student info not found - custom exception types
# Given a main program that searches for the ID or the name of a 
# student from a dictionary, complete the findID() and the 
# findName() functions that return the corresponding information 
# of a student. Then, insert a try/except statement in main() to 
# catch any exceptions thrown by findID() or findName(), and 
# output the exception message. Each entry of the dictionary 
# contains the name (key) and the ID (value) of a student.
#
# Function findID() takes two parameters, a student's name and 
# a dictionary. Function findID() returns the ID associated with 
# the student's name if the name is in the dictionary. Otherwise, 
# the function throws a custom exception type, StudentInfoError, 
# with the message "Student ID not found for studentName", where 
# studentName is the name of the student.
#
# Function findName() takes two parameters, a student's ID and 
# a dictionary. Function findName() returns the name associated 
# with the student's ID if the ID is in the dictionary. Otherwise, 
# the function throws a custom exception type, StudentInfoError, 
# with the message "Student name not found for studentID", where 
# studentID is the ID of the student.
#
# The main program takes two inputs from a user: a user choice of 
# finding the ID or the name of a student (int), and the ID or 
# the name of a student (string). If the user choice is 0, 
# findID() is invoked with the student's name as one of the 
# arguments. If the user choice is 1, findName() is invoked with 
# the student's ID as one of the arguments. The main program 
# finally outputs the result of the search or a message if an 
# exception is caught.
#
# Note: StudentInfoError is defined in the program as a custom 
# exception type. StudentInfoError has an attribute to store an 
# exception message.
#
# Ex: If the input of the program is:
#
# 0
# Reagan
# and the contents of dictionary are:
#
# 'Reagan' : 'rebradshaw835',
# 'Ryley' : 'rbarber894',
# 'Peyton' : 'pstott885',
# 'Tyrese' : 'tmayo945',
# 'Caius' : 'ccharlton329'
# the output of the program is:
#
# rebradshaw835
# Ex: If the input of the program is:
#
# 0
# Mcauley
# the program outputs an exception message:
#
# Student ID not found for Mcauley
# Ex: If the input of the program is:
#
# 1
# rebradshaw835
# the output of the program is:
#
# Reagan
# Ex: If the input of the program is:
#
# 1
# mpreston272
# the program outputs an exception message:
#
# Student name not found for mpreston272

import ast
import json

class StudentInfoError(Exception):
    def __init__(self, message):
        self.message = message

def findID(name, studentInfo):
    if name in studentInfo:
        return studentInfo[name]
    raise StudentInfoError("Student ID not found for " + name)

def findName(ID, studentInfo):
    for name in studentInfo:
        if ID == studentInfo[name]:
            return name
    raise StudentInfoError("Student name not found for " + ID)

def loadDictionary():
    file = open('studentInfo.txt', 'r')
    contents = file.read()
    studentInfo = ast.literal_eval(contents)
    file.close()
    return studentInfo 

def addNewStudent(studentInfo):
    newStudentName = input('Please insert name: ')
    newStudentID = input('Please insert desired ID: ')
    studentInfo[newStudentName] = newStudentID
    with open('studentInfo.txt', 'w') as f:
        f.write(json.dumps(studentInfo))
    runMain()

def chooseFindNameOrID(studentInfo):
    userChoice = input('Would you like to:\n1) Search by student name\n2) Search by student ID\n3) Add a new student\n> ')
    try:
        if userChoice == "1":
            name = input('Please enter a name: > ')
            result = findID(name, studentInfo)
        elif userChoice == "2":
            ID = input('Please enter a student ID: > ')
            result = findName(ID, studentInfo)
        elif userChoice == "3":
            addNewStudent(studentInfo)
        else:
            return chooseFindNameOrID()
        print(result)
    except StudentInfoError as excpt:
        print(excpt)    

def runAgain():
    startAgain = input("Would you like to perform another search? (Y/N)? > ")
    if(startAgain.lower() == "y"):
        runMain()
    elif(startAgain.lower() == "n"):
        print("Exiting program.")
        exit()
    else:
        return runAgain()

def runMain():
    studentInfo = loadDictionary()
    chooseFindNameOrID(studentInfo)
    runAgain()

if __name__ == '__main__':
    runMain()
    