FAHRENHEIT_TO_CELSIUS_FACTOR = 5 / 9
CELSIUS_TO_FAHRENHEIT_FACTOR = 9 / 5

def convert_to_celsius(fahrenheit):
    return (fahrenheit - 32) * FAHRENHEIT_TO_CELSIUS_FACTOR

def convert_to_fahrenheit(celsius):
    return (celsius * CELSIUS_TO_FAHRENHEIT_FACTOR) + 32

try:
    temperature = float(input("Enter the temperature: "))
    unit = input("Enter the unit (C/F): ").strip().upper()

    if unit == "C":
        result = convert_to_fahrenheit(temperature)
        print(f"{temperature} Celsius is equal to {result} Fahrenheit.")
    elif unit == "F":
        result = convert_to_celsius(temperature)
        print(f"{temperature} Fahrenheit is equal to {result} Celsius.")
    else:
        print("Invalid unit. Please enter 'C' for Celsius or 'F' for Fahrenheit.")
except ValueError:
    print("Invalid temperature. Please enter a number.")
