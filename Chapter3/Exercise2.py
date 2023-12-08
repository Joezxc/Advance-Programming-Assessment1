import tkinter as tk
from tkinter import messagebox

def show_order():
    message = f"Your {coffee_choice.get()} with {sugar_choice.get()} sugar and {milk_choice.get()} milk will be served. Thank you!"
    messagebox.showinfo("Order Confirmation", message)

# Create the main window
root = tk.Tk()
root.title("Coffee Vending Machine")

coffee_choice = tk.StringVar()
sugar_choice = tk.StringVar()
milk_choice = tk.StringVar()

def create_vending_machine():
    # Coffee Selection
    coffee_frame = tk.Frame(root)
    coffee_frame.pack()

    coffee_label = tk.Label(coffee_frame, text="Select your coffee:")
    coffee_label.pack(side="left")

    coffee_menu = tk.OptionMenu(coffee_frame, coffee_choice, "Espresso", "Latte", "Cappuccino")
    coffee_menu.pack(side="left")

    # Sugar Selection
    sugar_frame = tk.Frame(root)
    sugar_frame.pack()

    sugar_label = tk.Label(sugar_frame, text="Select sugar level:")
    sugar_label.pack(side="left")

    sugar_menu = tk.OptionMenu(sugar_frame, sugar_choice, "No sugar", "Little sugar", "Regular sugar")
    sugar_menu.pack(side="left")

    # Milk Selection
    milk_frame = tk.Frame(root)
    milk_frame.pack()

    milk_label = tk.Label(milk_frame, text="Select milk option:")
    milk_label.pack(side="left")

    milk_menu = tk.OptionMenu(milk_frame, milk_choice, "No milk", "Regular milk", "Soy milk")
    milk_menu.pack(side="left")

    # Order Button
    order_button = tk.Button(root, text="Place Order", command=show_order)
    order_button.pack()

create_vending_machine()

root.mainloop()