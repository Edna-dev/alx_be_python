FAHRENHEIT_TO_CELSIUS_FACTOR = 5 / 9
CELSIUS_TO_FAHRENHEIT_FACTOR = 9 / 5

def convert_to_celsius(fahrenheit):
    return (fahrenheit - 32) * FAHRENHEIT_TO_CELSIUS_FACTOR

def convert_to_fahrenheit(celsius):
    return (celsius * CELSIUS_TO_FAHRENHEIT_FACTOR) + 32

def main():
    try:
        temperature = float(input("Enter temperature: "))
        unit = input("Enter unit (C/F): ").strip().upper()

        if unit == "C":
            result = convert_to_fahrenheit(temperature)
            print(f"{temperature}C is {result}F")
        elif unit == "F":
            result = convert_to_celsius(temperature)
            print(f"{temperature}F is {result}C")
        else:
            print("Invalid unit. Please enter C or F.")
    except ValueError:
        print("Invalid input. Please enter a numeric temperature.")

if __name__ == "__main__":
    main()
