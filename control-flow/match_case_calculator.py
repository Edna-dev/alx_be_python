# match_case_calculator.py

# Prompt user for two numbers
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))

# Prompt for the operation
operation = input("Choose the operation (+, -, *, /): ")

# Match-case block to handle operations
match operation:
    case '+':
        result = num1 + num2
        print(f"The result is {result}.")
    case '-':
        result = num1 - num2
        print(f"The result is {result}.")
    case '*':
        result = num1 * num2
        print(f"The result is {result}.")
    case '/':
        if num2 == 0:
            print("Cannot divide by zero.")
        else:
            result = num1 / num2
            print(f"The result is {result}.")
    case _:
        print("Invalid operation selected.")
Enter the first number: 10
Enter the second number: 5
Choose the operation (+, -, *, /): *
The result is 50.0.
Enter the first number: 10
Enter the second number: 0
Choose the operation (+, -, *, /): /
Cannot divide by zero.
