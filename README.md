# Calculator-Python
This repository contains different versions of a Calculator built in Python, designed to demonstrate progressive enhancements in functionality and user experience. The project is structured to show the evolution from a simple terminal-based calculator to a full-fledged GUI application, including an executable version.

#Versions included:

Basic Terminal Calculator – A simple Python script that performs arithmetic operations and displays results in the terminal.

Enhanced Terminal Calculator – An improved version with additional features while still operating in the terminal.

GUI Calculator – A user-friendly graphical interface built with Python, making the calculator more interactive and visually appealing.

Executable Version (.exe) – A compiled version of the GUI calculator for easy use without requiring Python installation.

This project is ideal for beginners learning Python, GUI development, and software packaging. It also serves as a practical demonstration of how projects can evolve step by step, from simple scripts to fully packaged applications.

#To make any of this file as a Desktop app (.exe file), a standalone app that anyone can run on Windows, without needing Python installed.
#Run the following commands in terminal, cmd etc

pip install pyinstaller
cd C:\Users\YourName\Documents\PythonProjects (Use cd to go to the folder where your calculator_gui.py file is saved. For example:)
pyinstaller --onefile --windowed calculator_gui.py

After PyInstaller finishes, go to the dist folder inside your project directory.

You’ll see calculator_gui.exe — this is your standalone calculator!

You can now share this .exe with anyone — they don’t need Python installed

#Optional tips for a polished app
Run pyinstaller --onefile --windowed --icon=calculator.ico calculator_gui.py (Make sure calculator.ico is in the same folder as your Python file.)

