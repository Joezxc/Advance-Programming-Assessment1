import tkinter as tk

def draw_shape():
    canvas.delete("all")
    shape = shape_var.get()

    if shape == "Oval":
        canvas.create_oval(50, 50, 250, 150, outline="black", width=2)
    elif shape == "Rectangle":
        canvas.create_rectangle(50, 50, 250, 150, outline="black", width=2)
    elif shape == "Square":
        canvas.create_rectangle(50, 50, 150, 150, outline="black", width=2)
    elif shape == "Triangle":
        canvas.create_polygon(50, 150, 250, 150, 150, 50, outline="black", width=2)

root = tk.Tk()
root.title("Shape Drawer")

shape_var = tk.StringVar()

shape_label = tk.Label(root, text="Select a shape:")
shape_label.pack()

shape_choices = ["Oval", "Rectangle", "Square", "Triangle"]

for shape in shape_choices:
    shape_radio = tk.Radiobutton(root, text=shape, variable=shape_var, value=shape)
    shape_radio.pack()

draw_button = tk.Button(root, text="Draw Shape", command=draw_shape)
draw_button.pack()

canvas = tk.Canvas(root, width=300, height=200, bg="white")
canvas.pack()

root.mainloop()