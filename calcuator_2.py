def arcsine ():
    while True:
        x = input("Select mode:\n1. in radians\n2. in degrees\n") #input to select the mode
        if x == "1":
            number = float(input("Enter a number: "))
            try: #to check if the entered number is valid; is can parsed to floating value or not
                number = sp.sympify(number)
                print("The result is: ", math.asin(number))
                return True
            except ValueError: #else printing the error statement
                print("Enter a valid number")
                return False
        elif x == "2": #if user selects degree mode
            try:
                number = float(input("Enter a number: "))
                print("The result is: ", math.asin(math.radians(number))) #converting degree to radians
                return True
            except ValueError:
                print("Enter a valid number")
                return False
        else: #if user selects mode other than 1 or 2
            print("Invalid input") #the loop continues

def arccosine ():
    while True:
        x = input("Select mode:\n1. in radians\n2. in degrees\n") #input to select the mode
        if x == "1":
            number = float(input("Enter a number: "))
            try: #to check if the entered number is valid; is can parsed to floating value or not
                number = sp.sympify(number)
                print("The result is: ", math.acos(number))
                return True
            except ValueError: #else printing the error statement
                print("Enter a valid number")
                return False
        elif x == "2": #if user selects degree mode
            try:
                number = float(input("Enter a number: "))
                print("The result is: ", math.acos(math.radians(number))) #converting degree to radians
                return True
            except ValueError:
                print("Enter a valid number")
                return False
        else: #if user selects mode other than 1 or 2
            print("Invalid input") #the loop continues

def arctangent ():
    while True:
        x = input("Select mode:\n1. in radians\n2. in degrees\n") #input to select the mode
        if x == "1":
            number = float(input("Enter a number: "))
            try: #to check if the entered number is valid; is can parsed to floating value or not
                number = sp.sympify(number)
                print("The result is: ", math.atan(number))
                return True
            except ValueError: #else printing the error statement
                print("Enter a valid number")
                return False
        elif x == "2": #if user selects degree mode
            try:
                number = float(input("Enter a number: "))
                print("The result is: ", math.atan(math.radians(number))) #converting degree to radians
                return True
            except ValueError:
                print("Enter a valid number")
                return False
        else: #if user selects mode other than 1 or 2
            print("Invalid input") #the loop continues
