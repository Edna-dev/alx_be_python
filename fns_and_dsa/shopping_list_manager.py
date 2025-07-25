def display_menu():
    print("Shopping List Manager")
    print("1. Add Item")
    print("2. Remove Item")
    print("3. View List")
    print("4. Exit")

shopping_list = []

display_menu()

choice = input("Enter your choice (number): ")

# Ensure the input is treated as a number
try:
    choice = int(choice)
except ValueError:
    print("Invalid input. Please enter a number.")

