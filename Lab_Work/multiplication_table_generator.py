# 5. Multiplication Table Generator

def print_table(number):
    if number < 0:
        print("Negative numbers are not allowed")
    else:
        print(f"Multiplication Table of {number}")
        for multiplier in range(1, 11):
            print(f"{number} x {multiplier} = {number * multiplier}")

number = int(input("Enter a number: "))
print_table(number)
