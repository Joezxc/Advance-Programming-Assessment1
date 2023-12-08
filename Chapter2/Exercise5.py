from tkinter import *

# Create a fuction that solves the equation
def calculate():
    try:
        # Checking the division by zero case
        if operator.get() == "/" and float(operand2.get()) == 0:
            result.set("Error! Division by zero.")
        else:
            result.set(eval(operand1.get() + operator.get() + operand2.get()))
    except Exception as e:
        result.set("Error! " + str(e))

# Function to clear the result
def clear():
    operand1.delete(0, END)
    operand2.delete(0, END)
    result.set("")

# Creating the application
app = Tk()
app.title("Arithmetic Operations")

# Creating widgets
operand1 = Entry(app)
operand1.grid(row=0, column=0)

operator = StringVar()
OptionMenu(app, operator, "+", "-", "*", "/", "%").grid(row=0, column=1)

operand2 = Entry(app)
operand2.grid(row=0, column=2)

calculate_button = Button(app, text="Calculate", command=calculate)
calculate_button.grid(row=1, column=0)

clear_button = Button(app, text="Clear", command=clear)
clear_button.grid(row=1, column=1)

result = StringVar()
Label(app, textvariable=result).grid(row=1, column=2)

# Starting the application
app.mainloop()