from tkinter import *

root = Tk()

# Create a 4 Arguments values for many widgets, including Frames for Borders and Background
button1 = Label(root, text="A", width=12, bg="red", relief=GROOVE , bd=5)
button2 = Label(root, text="B", width=12, bg="yellow")
button3 = Label(root, text="C", width=12, bg="blue")
button4 = Label(root, text="D", width=12, bg="white")

# Create a 4 button
button1.pack(side="top", fill=X)
button2.pack(side="bottom")
button3.pack(side="left", expand=1)
button4.pack(side="right")

root.mainloop()