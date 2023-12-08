import tkinter as tk
from tkinter import messagebox

class Students:
    def __init__(self, name, mark1, mark2, mark3):
        self.Name = name
        self.Mark1 = mark1
        self.Mark2 = mark2
        self.Mark3 = mark3

    def calcGrade(self):
        return (self.Mark1 + self.Mark2 + self.Mark3) / 3

    def display(self):
        grade = self.calcGrade()
        messagebox.showinfo('Student Details', f'Name: {self.Name}\nGrade: {grade}')

def on_click():
    name = name_entry.get()
    mark1 = int(mark1_entry.get())
    mark2 = int(mark2_entry.get())
    mark3 = int(mark3_entry.get())

    student = Students(name, mark1, mark2, mark3)
    student.display()

root = tk.Tk()

name_label = tk.Label(root, text='Enter student name:')
name_label.pack()

name_entry = tk.Entry(root)
name_entry.pack()

mark1_label = tk.Label(root, text='Enter mark1:')
mark1_label.pack()

mark1_entry = tk.Entry(root)
mark1_entry.pack()

mark2_label = tk.Label(root, text='Enter mark2:')
mark2_label.pack()

mark2_entry = tk.Entry(root)
mark2_entry.pack()

mark3_label = tk.Label(root, text='Enter mark3:')
mark3_label.pack()

mark3_entry = tk.Entry(root)
mark3_entry.pack()

button = tk.Button(root, text='Submit', command=on_click)
button.pack()

root.mainloop()