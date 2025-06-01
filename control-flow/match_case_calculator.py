# match_case_calculator.py

# Prompt for the first and second numbers
num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))

# Prompt for the operation
operation = input("Choose the operation (+, -, *, /): ")

# Perform the calculation using match-case (Python 3.10+)
match operation:
    case '+':
        result = num1 + num2
        print(f"The result is {result}")
    case '-':
        result = num1 - num2
        print(f"The result is {result}")
    case '*':
        result = num1 * num2
        print(f"The result is {result}")
    case '/':
        if num2 == 0:
            print("Error: Division by zero is not allowed.")
        else:
            result = num1 / num2
            print(f"The result is {result}")
    case _:
        print("Invalid operation selected. Please choose from +, -, *, or /.")
