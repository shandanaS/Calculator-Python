# Simple Calculator in Python

#Function for Addition
def add(x, y):
    return x + y

#Function for Subtraction
def subtract(x, y):
    return x - y

#Function for Multiplication
def multiply(x, y):
    return x * y

#Function for Division
def divide(x, y):
    if y == 0:
        return "Error! Division by zero is not allowed."
    return x / y

print("Simple Calculator")
print("----------------------")
print("Select operation:")
print("1. Add (+)")
print("2. Subtract (-)")
print("3. Multiply (*)")
print("4. Divide (/)")

# Get user choice
choice = input("Enter choice (1/2/3/4): ")

# Get numbers from user
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))

# Perform calculation
if choice == '1':
    print(f"The result is: {add(num1, num2)}")
elif choice == '2':
    print(f"The result is: {subtract(num1, num2)}")
elif choice == '3':
    print(f"The result is: {multiply(num1, num2)}")
elif choice == '4':
    print(f"The result is: {divide(num1, num2)}")
else:
    print("❌ Invalid input! Please choose a valid operation.")
