import math
#creating a class 
class Calculator:
#initialising 
    def __init__(self):
        self.calculation = ""
#creating a list to store calculation history 
        self.history = []
#creating a method that adds symbols to the calculation 
    def add_symbols(self, symbol):
        self.calculation += str(symbol)
#returning the calculation with the symbol 
        return self.calculation
#creating a method that evaluates calculation
    def evaluate_calculation(self):
#using the try and except block to either execute or handle erros 
        try:
#using eval() function to evaluate expression and convert it into string
            result = str(eval(self.calculation))
#appending a dictionary to self.history containing expression and result 
            self.history.append({"expression": self.calculation, "result": result})
#storing results of past calculations
            self.calculation = result  
#returning the result of the calculation
            return result
# returning a message and clearing the calculation if there is an error 
        except Exception:
            self.calculation = ""
            return "Error"
#creating a method that squares the numbers     
    def square(self):
        if self.calculation:
            self.calculation += "**2"  
        return self.calculation  
#creating a method that powers the numbers
    def power(self):
        if self.calculation:
            self.calculation += "**"  
        return self.calculation  
#creating a mehtod that uses pi    
    def pi(self):
        try:
#using the if statement to show error after clikcing = if nothing is added 
            if not self.calculation:  
                return "Error"
            result = str(float(self.calculation) * math.pi)
            self.history.append ({"expression" : self.calculation, "result π ": result })
            self.calcualtion = result
            return result
        except Exception:
            return "Error"
#creating a method that square roots the numbers       
    def square_root(self):
        try:
            if not self.calculation: 
                return "Error"
            num = float(self.calculation)
            if num < 0 :
                return "Error"
            result = str(math.sqrt(num))
            self.history.append ({"expression" : self.calculation, "result √ ": result })
            self.calculation = result
            return result
        except Exception:
            return "Error"
        
#creating a method to reset calculation string to an empty string
    def clear(self):
        self.calculation = ""
#returning empty string
        return self.calculation
    
# creating a method that gets all the calculations
    def all_history(self):
#returning all the expressions and results in a list of dictionaries
        return self.history
