import tkinter as tk
def main():
    root = tk.Tk()
    root.title("Welcome")

    # Generate a prefer font and size
    font_type = ("Sans Serif", 18, "bold")
    label = tk.Label(root, text="Welcome to my Sample App", font=font_type)
    label.pack(pady=20)

    # Set the default window size
    root.geometry("400x600")

    # Disable resizing the window
    root.resizable(0, 0)

    # Add background color to the Window
    root.configure(bg="wheat")

    root.mainloop()

if __name__ == "__main__":
    main()