# Modern GUI Calculator with History & Hover Effects (Corrected)

import tkinter as tk
from tkinter import messagebox

# Functions
history = []

def press(key):
    entry_var.set(entry_var.get() + str(key))

def clear():
    entry_var.set("")

def calculate():
    try:
        result = eval(entry_var.get())
        # Save expression and result to history
        history.append(entry_var.get() + " = " + str(result))
        entry_var.set(str(result))
        update_history()
    except ZeroDivisionError:
        messagebox.showerror("Error", "Division by zero is not allowed!")
        entry_var.set("")
    except:
        messagebox.showerror("Error", "Invalid Input!")
        entry_var.set("")

def update_history():
    history_text.config(state="normal")
    history_text.delete("1.0", tk.END)
    for item in history[-5:]:  # Show last 5 calculations
        history_text.insert(tk.END, item + "\n")
    history_text.config(state="disabled")

# Hover effect functions
def on_enter(e):
    e.widget['bg'] = "#6E6E6E"

def on_leave(e):
    if e.widget['text'] in operators:
        e.widget['bg'] = operator_bg
    elif e.widget['text'] == 'C':
        e.widget['bg'] = "#FF3B30"
    else:
        e.widget['bg'] = button_bg

# Main window
root = tk.Tk()
root.title("Modern Calculator")
root.geometry("400x550")
root.resizable(False, False)
root.configure(bg="#2C2C2C")

# Entry field
entry_var = tk.StringVar()
entry = tk.Entry(root, textvariable=entry_var, font=("Helvetica", 28), bd=0, relief="ridge",
                 justify="right", bg="#1E1E1E", fg="#FFFFFF", insertbackground="white")
entry.pack(fill="both", ipadx=8, pady=10, padx=10)

# History panel
history_text = tk.Text(root, height=5, font=("Helvetica", 12), bg="#1E1E1E", fg="#FFFFFF", state="disabled")
history_text.pack(fill="both", padx=10, pady=5)

# Button styles
button_font = ("Helvetica", 20)
button_bg = "#4B4B4B"
button_fg = "#FFFFFF"
operator_bg = "#FF9500"
operators = ['+', '-', '*', '/', '=']

# Corrected buttons layout
buttons = [
    ['C', '/', '*', '-'],
    ['7', '8', '9', '+'],
    ['4', '5', '6'],
    ['1', '2', '3'],
    ['0', '.', '=']
]

# Create buttons
for row in buttons:
    frame = tk.Frame(root, bg="#2C2C2C")
    frame.pack(expand=True, fill="both")
    for button in row:
        if button == '=':
            b = tk.Button(frame, text=button, font=button_font, bg=operator_bg, fg=button_fg, command=calculate)
        elif button in ['+', '-', '*', '/']:
            b = tk.Button(frame, text=button, font=button_font, bg=operator_bg, fg=button_fg,
                          command=lambda key=button: press(key))
        elif button == 'C':
            b = tk.Button(frame, text=button, font=button_font, bg="#FF3B30", fg=button_fg, command=clear)
        else:
            b = tk.Button(frame, text=button, font=button_font, bg=button_bg, fg=button_fg,
                          command=lambda key=button: press(key))
        b.pack(side="left", expand=True, fill="both", padx=5, pady=5)
        # Bind hover effects
        b.bind("<Enter>", on_enter)
        b.bind("<Leave>", on_leave)

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
