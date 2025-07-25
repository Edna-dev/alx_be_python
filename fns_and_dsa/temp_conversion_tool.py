#!/usr/bin/env python3

# Global conversion factors
FAHRENHEIT_SUBTRACT = 32
FAHRENHEIT_MULTIPLIER = 5 / 9
CELSIUS_MULTIPLIER = 9 / 5
CELSIUS_ADD = 32

# Convert Fahrenheit to Celsius
def convert_to_celsius(fahrenheit):
    return (fahrenheit - FAHRENHEIT_SUBTRACT) * FAHRENHEIT_MULTIPLIER

# Convert Celsius to Fahrenheit
def convert_to_fahrenheit(celsius):
    return (celsius * CELSIUS_MULTIPLIER) + CELSIUS_ADD

# Main user interaction function
def main():
    try:
        temp = float(input("Enter the temperature to convert: "))
        unit = input("Is this temperature in Celsius or Fahrenheit? (C/F): ").strip().upper()

        if unit == 'C':
            result = convert_to_fahrenheit(temp)
            print(f"{temp}°C is {result:.2f}°F")
        elif unit == 'F':
            result = convert_to_celsius(temp)
            print(f"{temp}°F is {result:.2f}°C")
        else:
            raise ValueError("Invalid unit. Please enter 'C' or 'F'.")

    except ValueError as e:
        print("Error:", e)

if __name__ == "__main__":
    main()
