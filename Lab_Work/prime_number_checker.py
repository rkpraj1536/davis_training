# 4. Prime Number Checker

def is_primeNo(number):
    if number <= 1:
        return False

    for divisor in range(2, number):
        if number % divisor == 0:
            return False

    return True

number = int(input("Enter a number: "))

if is_primeNo(number):
    print(f"{number} is a Prime Number")
else:
    print(f"{number} is Not a Prime Number")
