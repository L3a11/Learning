# Simple Calculator application in Python

# Function to add two numbers
def add(num1, num2):
    return num1 + num2

# Function to subtract two numbers
def subtract(num1, num2):
    return num1 - num2

# Function to multiply two numbers
def multiply(num1, num2):
    return num1 * num2

# Function to divide two numbers
def divide(num1, num2):
    if num2 == 0:
        return "Error! Division by zero is not allowed."
    else:
        return num1 / num2

# Main function to get user input and perform calculations
def calculator():
    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))
    
    operation = input("Choose operation (+, -, *, /): ")
    
    if operation == '+':
        print("Result: ", add(num1, num2))
    elif operation == '-':
        print("Result: ", subtract(num1, num2))
    elif operation == '*':
        print("Result: ", multiply(num1, num2))
    elif operation == '/':
        print("Result: ", divide(num1, num2))
    else:
        print("Invalid operation. Please choose from +, -, *, /")

# Run the calculator function
calculator()

# I can copy and paste this code into a Python interpreter or a Python script file and run it to perform basic calculations. The user can input two numbers and choose an operation to perform
