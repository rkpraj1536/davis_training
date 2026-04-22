# 2. Number Classification System

def classify_number(number):
    if number > 0:
        print(f"{number} is Positive")
        if number % 2 == 0:
            print("It is Even")
        else:
            print("It is Odd")
    elif number < 0:
        print(f"{number} is Negative")
        if number % 2 == 0:
            print("It is Even")
        else:
            print("It is Odd")
    else:
        print("The number is Zero")

numbers = [10, -7, 0, 15, -20]

for value in numbers:
    classify_number(value)
    print()
