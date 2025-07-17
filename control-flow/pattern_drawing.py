# pattern_drawing.py

# Prompt user to enter the pattern size
size = int(input("Enter the size of the pattern: "))

# Validate input
while size <= 0:
    print("Please enter a positive integer.")
    size = int(input("Enter the size of the pattern: "))

# Initialize row counter
row = 0

# Outer while loop for each row
while row < size:
    # Inner for loop for each column
    for col in range(size):
        print("*", end="")
    print()  # Newline after each row
    row += 1
