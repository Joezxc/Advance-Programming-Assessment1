import tkinter as tk

# Create main window
root = tk.Tk()
root.geometry("500x400")

# Generate left frame
L_frame = tk.Frame(root, borderwidth=5)
L_frame.pack(side=tk.LEFT, expand=True, fill=tk.BOTH)

# Generate the right frame
R_frame = tk.Frame(root, borderwidth=5)
R_frame.pack(side=tk.RIGHT, expand=True, fill=tk.BOTH)

#  Create the following labels inside the frames. A and B inside the left frame. C and D inside the right frame
label_A = tk.Label(L_frame, text="A", border=30, bg="#22263d", fg="white")
label_B = tk.Label(L_frame, text="B", border=30)
label_C = tk.Label(R_frame, text="C", border=30)
label_D = tk.Label(R_frame, text="D", border=30, bg="#22263d", fg="white")


# Using a pack() labels A, B, C, and D inside their respective frames
label_A.pack(side=tk.TOP, expand=True, fill=tk.X)
label_B.pack(side=tk.BOTTOM, expand=True, fill=tk.X)
label_C.pack(side=tk.TOP, expand=True, fill=tk.X)
label_D.pack(side=tk.BOTTOM, expand=True, fill=tk.X)

# Start the tkinter event loop
root.mainloop()