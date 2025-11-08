# Stylish Advanced GUI Calculator

import tkinter as tk
from tkinter import messagebox

# Functions
def press(key):
    entry_var.set(entry_var.get() + str(key))

def clear():
    entry_var.set("")

def calculate():
    try:
        result = eval(entry_var.get())
        entry_var.set(str(result))
    except ZeroDivisionError:
        messagebox.showerror("Error", "Division by zero is not allowed!")
        entry_var.set("")
    except:
        messagebox.showerror("Error", "Invalid Input!")
        entry_var.set("")

# Main window
root = tk.Tk()
root.title("Stylish Calculator")
root.geometry("360x500")
root.resizable(False, False)
root.configure(bg="#2E2E2E")  # dark background

# Entry field
entry_var = tk.StringVar()
entry = tk.Entry(root, textvariable=entry_var, font=("Helvetica", 28), bd=0, relief="ridge",
                 justify="right", bg="#1E1E1E", fg="#FFFFFF", insertbackground="white")
entry.pack(fill="both", ipadx=8, pady=20, padx=10)

# Button styles
button_font = ("Helvetica", 20)
button_bg = "#4B4B4B"
button_fg = "#FFFFFF"
operator_bg = "#FF9500"

# Buttons layout
buttons = [
    ['C', '/', '*', '-'],
    ['7', '8', '9', '+'],
    ['4', '5', '6', '='],
    ['1', '2', '3', '='],
    ['0', '.', '=']
]

# Create frames and buttons
for row in buttons:
    frame = tk.Frame(root, bg="#2E2E2E")
    frame.pack(expand=True, fill="both")
    for button in row:
        if button == '=':
            b = tk.Button(frame, text=button, font=button_font, bg=operator_bg, fg=button_fg,
                          command=calculate)
        elif button in ['+', '-', '*', '/']:
            b = tk.Button(frame, text=button, font=button_font, bg=operator_bg, fg=button_fg,
                          command=lambda key=button: press(key))
        elif button == 'C':
            b = tk.Button(frame, text=button, font=button_font, bg="#FF3B30", fg=button_fg,
                          command=clear)
        else:
            b = tk.Button(frame, text=button, font=button_font, bg=button_bg, fg=button_fg,
                          command=lambda key=button: press(key))
        b.pack(side="left", expand=True, fill="both", padx=3, pady=3)

# Keyboard support
def key_press(event):
    if event.char.isdigit() or event.char in '+-*/.':
        press(event.char)
    elif event.keysym == "Return":
        calculate()
    elif event.keysym == "BackSpace":
        entry_var.set(entry_var.get()[:-1])
    elif event.keysym.lower() == "c":
        clear()

root.bind("<Key>", key_press)

# Run the app
root.mainloop()
