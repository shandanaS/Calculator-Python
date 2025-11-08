# GUI Simple Calculator using tkinter

import tkinter as tk
from tkinter import messagebox

# Functions for operations
def add():
    try:
        result = float(entry_num1.get()) + float(entry_num2.get())
        label_result.config(text=f"Result: {result}")
    except ValueError:
        messagebox.showerror("Error", "Please enter valid numbers.")

def subtract():
    try:
        result = float(entry_num1.get()) - float(entry_num2.get())
        label_result.config(text=f"Result: {result}")
    except ValueError:
        messagebox.showerror("Error", "Please enter valid numbers.")

def multiply():
    try:
        result = float(entry_num1.get()) * float(entry_num2.get())
        label_result.config(text=f"Result: {result}")
    except ValueError:
        messagebox.showerror("Error", "Please enter valid numbers.")

def divide():
    try:
        num2 = float(entry_num2.get())
        if num2 == 0:
            messagebox.showerror("Error", "Division by zero is not allowed!")
        else:
            result = float(entry_num1.get()) / num2
            label_result.config(text=f"Result: {result}")
    except ValueError:
        messagebox.showerror("Error", "Please enter valid numbers.")

# Create main window
root = tk.Tk()
root.title("Simple Calculator")
root.geometry("300x250")

# Input fields
tk.Label(root, text="First Number:").pack(pady=5)
entry_num1 = tk.Entry(root)
entry_num1.pack(pady=5)

tk.Label(root, text="Second Number:").pack(pady=5)
entry_num2 = tk.Entry(root)
entry_num2.pack(pady=5)

# Buttons
tk.Button(root, text="Add (+)", width=10, command=add).pack(pady=5)
tk.Button(root, text="Subtract (-)", width=10, command=subtract).pack(pady=5)
tk.Button(root, text="Multiply (*)", width=10, command=multiply).pack(pady=5)
tk.Button(root, text="Divide (/)", width=10, command=divide).pack(pady=5)

# Result label
label_result = tk.Label(root, text="Result: ", font=("Arial", 12))
label_result.pack(pady=10)

# Run the GUI loop
root.mainloop()
