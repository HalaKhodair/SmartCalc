import math
import sympy as sp #to handle expressions in radian to an integer
#this function returns the sin of a given input
def sine ():
    while True:
        x = input("Select mode:\n1. in radians\n2. in degrees\n") #input to select the mode
        if x == "1":
            number = (input("Enter a number: "))
            try: #to check if the entered number is valid; is can parsed to floating value or not
                number = sp.sympify(number) #converting expressions in radians to float
                print("The result is: ", math.sin(number))
                return True
            except ValueError: #raising an error if entered number is not in correct format
                print("Enter a valid number")
                return False
        elif x == "2": #if user selects degree mode
            try:  #to check if the entered number is valid; a floating value
                number = float(input("Enter a number: "))
                print("The result is: ", math.sin(math.radians(number)))#converting degree to radians
                return True
            except ValueError:
                print("Enter a valid number")
                return False
        else: #if user selects mode other than 1 or 2
            print("Invalid input")


#this function returns the sin of a given input
def cosine ():
    while True: #the functions continue to ask the mode selection if entered input in not correct
        x = input("Select mode:\n1. in radians\n2. in degrees\n")
        if x == "1":
            number = float(input("Enter a number: "))
            try:  #to check if the entered number is valid; it can be converted to float or not
                number = sp.sympify(number) #parsing the expression in radians to float value
                print("The result is: ", math.cos(number))
                return True
            except ValueError:
                print("Enter a valid number")
                return False
        elif x == "2":
            try:  #check if the entered number is valid; a floating value
                number = float(input("Enter a number: "))
                print("The result is: ", math.cos(math.radians(number)))
                return True
            except ValueError:
                print("Enter a valid number")
                return False
        else:
            print("Invalid input")

#this function returns tangent of a given input
def tangent ():
    while True:
        x = input("Select mode:\n1. in radians\n2. in degrees\n") #input to select the mode
        if x == "1":
            number = float(input("Enter a number: "))
            try: #to check if the entered number is valid; is can parsed to floating value or not
                number = sp.sympify(number)
                print("The result is: ", math.tan(number))
                return True
            except ValueError: #else printing the error statement
                print("Enter a valid number")
                return False
        elif x == "2": #if user selects degree mode
            try:
                number = float(input("Enter a number: "))
                print("The result is: ", math.tan(math.radians(number))) #converting degree to radians
                return True
            except ValueError:
                print("Enter a valid number")
                return False
        else: #if user selects mode other than 1 or 2
            print("Invalid input") #the loop continues
