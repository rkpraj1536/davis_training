# Question 18: Custom Module: Math Utility Package

# math_utils.py
def is_prime(number):
    if number < 2:
        return False
    for i in range(2, number):
        if number % i == 0:
            return False
    return True

def fibonacci(limit):
    sequence = [0, 1]
    while len(sequence) < limit:
        sequence.append(sequence[-1] + sequence[-2])
    return sequence

def factorial(number):
    result = 1
    for i in range(1, number + 1):
        result *= i
    return result

print(is_prime(7))
print(fibonacci(5))
print(factorial(5))
