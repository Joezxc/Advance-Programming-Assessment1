import tkinter as tk
import re

def check_password():
    global attempts
    password = password_entry.get()
    if len(password) < 6 or len(password) > 12:
        result_label.config(text="Password length should be between 6 and 12 characters")
    elif not re.search("[a-z]", password):
        result_label.config(text="Password should contain at least 1 lowercase letter")
    elif not re.search("[A-Z]", password):
        result_label.config(text="Password should contain at least 1 uppercase letter")
    elif not re.search("[0-9]", password):
        result_label.config(text="Password should contain at least 1 number")
    elif not re.search("[$#@]", password):
        result_label.config(text="Password should contain at least 1 of the symbols $, #, @")
    else:
        attempts -= 1
        if attempts == 0:
            result_label.config(text="All attempts used. The authorities have been alerted!")
        else:
            result_label.config(text=f"Correct password! You have {attempts} attempts remaining.")

# Create the main window
root = tk.Tk()
root.title("Password Checker App")

# Create the entry for password input
password_entry = tk.Entry(root)
password_entry.pack(pady=10)

# Create the check password button
check_password_button = tk.Button(root, text="Check Password", command=check_password)
check_password_button.pack(pady=10)

# Create the result label
result_label = tk.Label(root, text="")
result_label.pack(pady=10)

# Set the number of password attempts
attempts = 5

# Start the main loop
root.mainloop()