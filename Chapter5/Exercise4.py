import tkinter as tk
import math

class Shape:
    def inputSides(self):
        pass

class Circle(Shape):
    def __init__(self):
        self.radius = 0

    def inputSides(self):
        self.radius = float(entry_radius.get())

    def area(self):
        return math.pi * self.radius**2

class Rectangle(Shape):
    def __init__(self):
        self.length = 0
        self.width = 0

    def inputSides(self):
        self.length = float(entry_length.get())
        self.width = float(entry_width.get())

    def area(self):
        return self.length * self.width

class Triangle(Shape):
    def __init__(self):
        self.side1 = 0
        self.side2 = 0
        self.side3 = 0

    def inputSides(self):
        self.side1 = float(entry_side1.get())
        self.side2 = float(entry_side2.get())
        self.side3 = float(entry_side3.get())

    def area(self):
        s = (self.side1 + self.side2 + self.side3) / 2
        return math.sqrt(s * (s - self.side1) * (s - self.side2) * (s - self.side3))

def calculate_circle_area():
    circle = Circle()
    circle.inputSides()
    result_label.config(text=f"Area of the circle: {circle.area()}")

def calculate_rectangle_area():
    rectangle = Rectangle()
    rectangle.inputSides()
    result_label.config(text=f"Area of the rectangle: {rectangle.area()}")

def calculate_triangle_area():
    triangle = Triangle()
    triangle.inputSides()
    result_label.config(text=f"Area of the triangle: {triangle.area()}")

root = tk.Tk()
root.title("Area Calculator")

# Circle Inputs
label_radius = tk.Label(root, text="Enter Radius:")
label_radius.pack()
entry_radius = tk.Entry(root)
entry_radius.pack()

# Rectangle Inputs
label_length = tk.Label(root, text="Enter Length:")
label_length.pack()
entry_length = tk.Entry(root)
entry_length.pack()

label_width = tk.Label(root, text="Enter Width:")
label_width.pack()
entry_width = tk.Entry(root)
entry_width.pack()

# Triangle Inputs
label_side1 = tk.Label(root, text="Enter Side 1:")
label_side1.pack()
entry_side1 = tk.Entry(root)
entry_side1.pack()

label_side2 = tk.Label(root, text="Enter Side 2:")
label_side2.pack()
entry_side2 = tk.Entry(root)
entry_side2.pack()

label_side3 = tk.Label(root, text="Enter Side 3:")
label_side3.pack()
entry_side3 = tk.Entry(root)
entry_side3.pack()

# Calculate buttons
circle_button = tk.Button(root, text="Calculate Circle Area", command=calculate_circle_area)
circle_button.pack()

rectangle_button = tk.Button(root, text="Calculate Rectangle Area", command=calculate_rectangle_area)
rectangle_button.pack()

triangle_button = tk.Button(root, text="Calculate Triangle Area", command=calculate_triangle_area)
triangle_button.pack()

result_label = tk.Label(root, text="")
result_label.pack()

root.mainloop()