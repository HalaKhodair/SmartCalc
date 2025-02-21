import math
import tkinter as tk

# Creating the Calculator class
class Calculator:
    def __init__(self):
        self.calculation = ""  # Stores current input
        self.history = []  # Stores calculation history

    def add_symbols(self, symbol):
        """Appends symbols correctly, including trigonometric functions."""
        if symbol in ['cos', 'sin', 'tan', 'asin', 'acos', 'atan']:
            self.calculation += f'math.{symbol}('  # Ensures function calls work
        else:
            self.calculation += str(symbol)
        return self.calculation

    def evaluate_calculation(self):
        """Evaluates the mathematical expression."""
        try:
            result = str(eval(self.calculation))  # Safely evaluates the expression
            self.history.append({"expression": self.calculation, "result": result})
            self.calculation = result  # Store result for further operations
            return result
        except Exception:
            self.calculation = ""
            return "Error"

    def square(self):
        """Squares the current number."""
        if self.calculation:
            self.calculation += "**2"
        return self.calculation

    def power(self):
        """Adds exponentiation operator."""
        if self.calculation:
            self.calculation += "**"
        return self.calculation

    def pi(self):
        """Multiplies by π (pi)."""
        try:
            if not self.calculation:
                return "Error"
            result = str(float(self.calculation) * math.pi)
            self.history.append({"expression": self.calculation, "result π ": result})
            self.calculation = result
            return result
        except Exception:
            return "Error"

    def square_root(self):
        """Computes the square root."""
        try:
            if not self.calculation:
                return "Error"
            num = float(self.calculation)
            if num < 0:
                return "Error"
            result = str(math.sqrt(num))
            self.history.append({"expression": self.calculation, "result √ ": result})
            self.calculation = result
            return result
        except Exception:
            return "Error"

    def clear(self):
        """Clears the current input."""
        self.calculation = ""
        return self.calculation

    def all_history(self):
        """Returns the calculation history."""
        return self.history


# GUI Class
class CalculatorGUI:
    def __init__(self):
        self.calculator = Calculator()
        self.root = tk.Tk()
        self.root.title("Scientific Calculator")
        self.root.geometry("450x550")

        # Text field for displaying calculations
        self.text_result = tk.Text(self.root, height=3, width=15, font=("Arial", 30))
        self.text_result.grid(columnspan=10)

        self.create_buttons()

    def create_buttons(self):
        """Creates and places calculator buttons in the GUI."""
        buttons = [
            ("1", 2, 1), ("2", 2, 2), ("3", 2, 3),
            ("4", 3, 1), ("5", 3, 2), ("6", 3, 3),
            ("7", 4, 1), ("8", 4, 2), ("9", 4, 3),
            ("0", 5, 2), ("+", 2, 4), ("-", 3, 4),
            ("*", 4, 4), ("/", 5, 4), ("(", 5, 1),
            (")", 5, 3), ("C", 8, 1, 2), ("=", 8, 3, 2),
            ("^", 1, 1), ("π", 1, 2),  ("²", 1, 3), ("√", 1, 4),
            ("Sin", 6, 1), ("Cos", 6, 2), ("Tan", 6, 3), (".", 6, 4),
            ("asin", 7, 1), ("acos", 7, 2), ("atan", 7, 3)
        ]

        for btn_text, row, col, *span in buttons:
            if btn_text == "C":
                action = self.clear_field
            elif btn_text == "=":
                action = self.evaluate_calculation
            elif btn_text == "^":
                action = self.power
            elif btn_text == "π":
                action = self.pi
            elif btn_text == "²":
                action = self.square
            elif btn_text == "√":
                action = self.square_root
            elif btn_text in ["Sin", "Cos", "Tan", "ArcSin", "ArcCos", "ArcTan"]:
                action = lambda x=btn_text.lower(): self.add_symbols(x)  # Convert to lowercase
            else:
                action = lambda x=btn_text: self.add_symbols(x)

            button = tk.Button(self.root, text=btn_text, command=action, width=5, font=("Arial", 14))
            button.grid(row=row, column=col, columnspan=span[0] if span else 1, sticky="nsew")

        for r in range(1, 9):
            self.root.grid_rowconfigure(r, weight=1)
        for c in range(1, 5):
            self.root.grid_columnconfigure(c, weight=1)

    def add_symbols(self, symbol):
        """Adds the symbol to the calculation and updates display."""
        result = self.calculator.add_symbols(symbol)
        self.update_display(result)

    def evaluate_calculation(self):
        """Evaluates the calculation and updates the result."""
        result = self.calculator.evaluate_calculation()
        self.update_display(result)

    def square(self):
        """Calculates square."""
        result = self.calculator.square()
        self.update_display(result)

    def power(self):
        """Adds exponentiation symbol."""
        result = self.calculator.power()
        self.update_display(result)

    def pi(self):
        """Handles π multiplication."""
        result = self.calculator.pi()
        self.update_display(result)

    def square_root(self):
        """Calculates square root."""
        result = self.calculator.square_root()
        self.update_display(result)

    def clear_field(self):
        """Clears the display."""
        result = self.calculator.clear()
        self.update_display(result)

    def update_display(self, text):
        """Updates the GUI display with the latest input or result."""
        self.text_result.delete(1.0, "end")
        self.text_result.insert("end", text)
        self.text_result.see("end")

    def run(self):
        """Starts the Tkinter event loop."""
        self.root.mainloop()


# Run the Calculator GUI
if __name__ == "__main__":
    calc = CalculatorGUI()
    calc.run()

