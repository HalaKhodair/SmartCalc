#Importing tkniter for creating GUI
import tkinter as tk
#importing Calculator class from the other file
from my_calculator import Calculator
#defining GUI class 
class CalculatorGUI:
#initialising an instance of the calculator class
    def __init__(self):
        self.calculator = Calculator()
#creating a window for the application
        self.root = tk.Tk()
#applying a suitable size for the window
        self.root.geometry("420x550")
#creating a text widget for the calculation and results
        self.text_result = tk.Text(self.root, height=3, width=15, font=("Arial", 30))
#Adjusting the columnspan to align with the button layout
        self.text_result.grid(columnspan=4)
#creating and placing calculator buttons
        self.create_buttons() 
#defining method to create buttons ans place them on the GUI
    def create_buttons(self):
#creating a list that conatins the button's labels and positions
        buttons = [
            ("1", 2, 1), ("2", 2, 2), ("3", 2, 3),
            ("4", 3, 1), ("5", 3, 2), ("6", 3, 3),
            ("7", 4, 1), ("8", 4, 2), ("9", 4, 3),
            ("0", 5, 2), ("+", 2, 4), ("-", 3, 4),
            ("*", 4, 4), ("/", 5, 4), ("(", 5, 1),
            (")", 5, 3), ("C", 6, 1, 2), ("=", 6, 3, 2),
            ("x²", 1, 3),  ("√x", 1, 4) ]
             
#using for loop to iterate through the button list
        for btn_text, row, col, *span in buttons:
#using if statement to reset current calculation when C is clicked
            if btn_text == "C":
                action = self.clear_field
#evaluating the calculation if equal is clicked
            else:
                btn_text == "="
                action = self.evaluate_calculation
#executing other buttons by calling the add symbol method
#using lambda to delay execution until button is clicked
#storing button text as variable "x"
                action = lambda x=btn_text: self.add_symbols(x)

 # Adjusting button width and grid to aligin them correctly 
            button = tk.Button(self.root, text=btn_text, command=action, width=5, font=("Arial", 14))
            button.grid(row=row, column=col, columnspan=span[0] if span else 1, sticky="nsew")
        
# ensuring buttons expand proportionally in the grid using for loop
#using for loop to iterate through rows 1 to 6
        for r in range(1, 7):
#expanding all rows equally when window is resized vertically
            self.root.grid_rowconfigure(r, weight=1)
#using for loop to iterate through columns 1 to 4
        for c in range(1, 5):
#expanding all columns equally when window is resized horizontally
            self.root.grid_columnconfigure(c, weight=1)
#defining the adding symbols method
    def add_symbols(self, symbol):
#adding symbol to ongoing calculations and updating the display
        result = self.calculator.add_symbols(symbol)
        self.update_display(result)
#defining ealuate method to evaluate the calculations and update the results
    def evaluate_calculation(self):
        result = self.calculator.evaluate_calculation()
        self.update_display(result)
#defining the clear_feild method
    def clear_field(self):
#clearing current calculation using calculator class and updating the display
        result = self.calculator.clear()
        self.update_display(result)
#defining the update_display method 
    def update_display(self, text):
#clearing the ongoing calculation or results
        self.text_result.delete(1.0, "end")
#inserting new calculations or expresssions
        self.text_result.insert(1.0, text)

    
#defining the run method to strat the tkinter event loop
    def run(self):
        self.root.mainloop()
#ensuring application runs only when the GUI file is executed directly
if __name__ == "__main__":
#creating an instance of the CalculatorGUI class
    calc = CalculatorGUI()
#starting the GUI application
    calc.run()
