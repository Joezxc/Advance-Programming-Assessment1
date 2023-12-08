from tkinter import *

# Function to convert the temperature
def convert():
    try:
        if variable.get() == "Celsius to Fahrenheit":
            result.set(eval(temperature.get()) * 9/5 + 32)
        else:
            result.set(eval(temperature.get()) - 32) * 5/9
    except Exception as e:
        result.set("Error! " + str(e))

# Function to clear the result
def clear():
    temperature.delete(0, END)
    result.set("")

# Creating the application
app = Tk()
app.title("Temperature Converter")

# Creating widgets
variable = StringVar()
OptionMenu(app, variable, "Celsius to Fahrenheit", "Fahrenheit to Celsius").grid(row=0, column=0)

temperature = Entry(app)
temperature.grid(row=0, column=1)

convert_button = Button(app, text="Convert", command=convert)
convert_button.grid(row=1, column=0)

clear_button = Button(app, text="Clear", command=clear)
clear_button.grid(row=1, column=1)

result = StringVar()
Label(app, textvariable=result).grid(row=1, column=2)

# Starting the application
app.mainloop()