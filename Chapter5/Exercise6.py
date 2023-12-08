from tkinter import *
from tkinter import messagebox

class ArithmeticOperations:
    def __init__(self, master):
        self.master = master
        self.master.title("Arithmetic Operations")

        self.result = StringVar()

        # Creating label
        Label(self.master, text='First Number:').grid(row=0, column=0)
        Label(self.master, text='Second Number:').grid(row=1, column=0)
        Label(self.master, text='Result:').grid(row=2, column=0)

        # Creating entry
        self.first_number = Entry(self.master)
        self.second_number = Entry(self.master)
        self.result_entry = Entry(self.master, textvariable=self.result)

        self.first_number.grid(row=0, column=1)
        self.second_number.grid(row=1, column=1)
        self.result_entry.grid(row=2, column=1)

        # Creating buttons
        Button(self.master, text='Add', command=self.add).grid(row=0, column=2)
        Button(self.master, text='Subtract', command=self.subtract).grid(row=1, column=2)
        Button(self.master, text='Multiply', command=self.multiply).grid(row=2, column=2)
        Button(self.master, text='Divide', command=self.divide).grid(row=3, column=1)

    def add(self):
        try:
            result = int(self.first_number.get()) + int(self.second_number.get())
            self.result.set(result)
        except ValueError:
            messagebox.showerror('Error', 'Invalid input. Please enter numbers.')

    def subtract(self):
        try:
            result = int(self.first_number.get()) - int(self.second_number.get())
            self.result.set(result)
        except ValueError:
            messagebox.showerror('Error', 'Invalid input. Please enter numbers.')

    def multiply(self):
        try:
            result = int(self.first_number.get()) * int(self.second_number.get())
            self.result.set(result)
        except ValueError:
            messagebox.showerror('Error', 'Invalid input. Please enter numbers.')

    def divide(self):
        try:
            if int(self.second_number.get()) == 0:
                messagebox.showerror('Error', 'Division by zero is not allowed.')
            else:
                result = int(self.first_number.get()) / int(self.second_number.get())
                self.result.set(result)
        except ValueError:
            messagebox.showerror('Error', 'Invalid input. Please enter numbers.')

# Running the program
if __name__ == '__main__':
    root = Tk()
    arithmetic = ArithmeticOperations(root)
    root.mainloop()