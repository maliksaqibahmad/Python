import math

def show_menu():
    print("\nScientific Calculator Menu:")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    print("5. Power")
    print("6. Square Root")
    print("7. Sine")
    print("8. Cosine")
    print("9. Tangent")
    print("10. Logarithm (base e)")
    print("11. Exponential (e^x)")
    print("0. Exit")

def get_valid_number(prompt):
    while True:
        try:
            num = float(input(prompt))
            return num
        except ValueError:
            print("Invalid input. Please enter a valid number.")

def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b != 0:
        return a / b
    else:
        print("Error: Division by zero")
        return None

def power(base, exponent):
    return math.pow(base, exponent)

def square_root(a):
    return math.sqrt(a)

def sine(angle):
    return math.sin(math.radians(angle))

def cosine(angle):
    return math.cos(math.radians(angle))

def tangent(angle):
    return math.tan(math.radians(angle))

def logarithm(a):
    return math.log(a)

def exponential(a):
    return math.exp(a)

def main():
    while True:
        show_menu()
        choice = input("Choose an operation: ")

        if choice == '0':
            print("Exiting...")
            break

        if choice in ['1', '2', '3', '4', '5']:
            num1 = get_valid_number("Enter first number: ")
            num2 = get_valid_number("Enter second number: ")

            if choice == '1':
                print("Result:", add(num1, num2))
            elif choice == '2':
                print("Result:", subtract(num1, num2))
            elif choice == '3':
                print("Result:", multiply(num1, num2))
            elif choice == '4':
                result = divide(num1, num2)
                if result is not None:
                    print("Result:", result)
            elif choice == '5':
                print("Result:", power(num1, num2))

        elif choice == '6':
            num = get_valid_number("Enter a number: ")
            print("Result:", square_root(num))

        elif choice in ['7', '8', '9']:
            angle = get_valid_number("Enter an angle in degrees: ")
            if choice == '7':
                print("Result:", sine(angle))
            elif choice == '8':
                print("Result:", cosine(angle))
            elif choice == '9':
                print("Result:", tangent(angle))

        elif choice == '10':
            num = get_valid_number("Enter a number: ")
            print("Result:", logarithm(num))

        elif choice == '11':
            num = get_valid_number("Enter a number: ")
            print("Result:", exponential(num))

        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()