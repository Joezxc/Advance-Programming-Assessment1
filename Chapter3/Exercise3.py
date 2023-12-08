import tkinter as tk
from tkinter import ttk, messagebox

def calculate_circle_area():
    try:
        radius = float(circle_radius_entry.get())
        area = 3.14159 * (radius ** 2)
        circle_area_label.config(text=f"Area of the circle: {area}")
    except ValueError:
        messagebox.showerror("Error", "Please enter a valid number for radius.")

def calculate_square_area():
    try:
        side = float(square_side_entry.get())
        area = side ** 2
        square_area_label.config(text=f"Area of the square: {area}")
    except ValueError:
        messagebox.showerror("Error", "Please enter a valid number for side length.")

def calculate_rectangle_area():
    try:
        length = float(rectangle_length_entry.get())
        width = float(rectangle_width_entry.get())
        area = length * width
        rectangle_area_label.config(text=f"Area of the rectangle: {area}")
    except ValueError:
        messagebox.showerror("Error", "Please enter valid numbers for length and width.")

root = tk.Tk()
root.title("Area Calculator")

tab_control = ttk.Notebook(root)

circle_tab = ttk.Frame(tab_control)
square_tab = ttk.Frame(tab_control)
rectangle_tab = ttk.Frame(tab_control)

tab_control.add(circle_tab, text='Circle')
tab_control.add(square_tab, text='Square')
tab_control.add(rectangle_tab, text='Rectangle')

# Circle tab widgets
circle_radius_label = tk.Label(circle_tab, text="Enter radius:")
circle_radius_label.pack()
circle_radius_entry = tk.Entry(circle_tab)
circle_radius_entry.pack()
circle_calculate_button = tk.Button(circle_tab, text="Calculate", command=calculate_circle_area)
circle_calculate_button.pack()
circle_area_label = tk.Label(circle_tab, text="")
circle_area_label.pack()

# Square tab widgets
square_side_label = tk.Label(square_tab, text="Enter side length:")
square_side_label.pack()
square_side_entry = tk.Entry(square_tab)
square_side_entry.pack()
square_calculate_button = tk.Button(square_tab, text="Calculate", command=calculate_square_area)
square_calculate_button.pack()
square_area_label = tk.Label(square_tab, text="")
square_area_label.pack()

# Rectangle tab widgets
rectangle_length_label = tk.Label(rectangle_tab, text="Enter length:")
rectangle_length_label.pack()
rectangle_length_entry = tk.Entry(rectangle_tab)
rectangle_length_entry.pack()
rectangle_width_label = tk.Label(rectangle_tab, text="Enter width:")
rectangle_width_label.pack()
rectangle_width_entry = tk.Entry(rectangle_tab)
rectangle_width_entry.pack()
rectangle_calculate_button = tk.Button(rectangle_tab, text="Calculate", command=calculate_rectangle_area)
rectangle_calculate_button.pack()
rectangle_area_label = tk.Label(rectangle_tab, text="")
rectangle_area_label.pack()

tab_control.pack(expand=1, fill="both")

root.mainloop()