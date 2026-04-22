# 10. Menu Driven Calculator

def add(number1, number2):
    return number1 + number2

def subtract(number1, number2):
    return number1 - number2

def multiply(number1, number2):
    return number1 * number2

def divide(number1, number2):
    if number2 == 0:
        return "Cannot divide by zero"
    return number1 / number2

while True:
    print("\n----- Calculator Menu -----")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")
    print("5. Exit")

    choice = input("Enter your choice: ")

    if choice == "5":
        print("Calculator Closed")
        break

    elif choice in ["1", "2", "3", "4"]:
        number1 = float(input("Enter first number: "))
        number2 = float(input("Enter second number: "))

        if choice == "1":
            print("Result =", add(number1, number2))
        elif choice == "2":
            print("Result =", subtract(number1, number2))
        elif choice == "3":
            print("Result =", multiply(number1, number2))
        elif choice == "4":
            print("Result =", divide(number1, number2))
    else:
        print("Invalid Choice. Please select between 1 and 5.")
