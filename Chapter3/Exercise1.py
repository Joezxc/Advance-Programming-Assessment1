import tkinter as tk
from tkinter import ttk

class App(tk.Tk):
    def __init__(self):
        super().__init__()

        self.title("Greeting App")
        self.geometry("400x300")

        self.input_frame = ttk.Frame(self, padding=(10, 10, 10, 10))
        self.input_frame.pack(fill=tk.BOTH, expand=True)

        self.display_frame = ttk.Frame(self, padding=(10, 10, 10, 10))
        self.display_frame.pack(fill=tk.BOTH, expand=True)

        self.name_var = tk.StringVar()
        self.color_var = tk.StringVar()

        name_label = ttk.Label(self.input_frame, text="Enter your name:")
        name_label.pack()

        name_entry = ttk.Entry(self.input_frame, textvariable=self.name_var)
        name_entry.pack()

        color_label = ttk.Label(self.input_frame, text="Select a color:")
        color_label.pack()

        color_option = ttk.Combobox(self.input_frame, textvariable=self.color_var, values=("red", "blue", "green", "yellow", "orange", "purple"), state="readonly")
        color_option.pack()

        update_button = ttk.Button(self.input_frame, text="Update Greeting", command=self.update_greeting)
        update_button.pack()

        self.display_label = ttk.Label(self.display_frame, text="")
        self.display_label.pack()

    def update_greeting(self):
        name = self.name_var.get()
        color = self.color_var.get()

        if name:
            greeting = f"Hello, {name}! Nice to meet you!"
            self.display_label.config(text=greeting, foreground=color)
        else:
            self.display_label.config(text="")

if __name__ == "__main__":
    app = App()
    app.mainloop()