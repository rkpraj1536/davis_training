import numpy as np

try:
    # input number
    n = int(input("Enter a number: "))

    # check for zero
    if n == 0:
        print("Enter number greater than 0")
    
    # check for negative number
    elif n < 0:
        print("Negative number is not allowed")
        n = abs(n)

        even_factors = [i for i in range(1, n + 1) if n % i == 0 and i % 2 == 0]
        array = np.array(even_factors)

        print("Even factors:", even_factors)
        print("NumPy array:", array)

    else:
        # normal case
        even_factors = [i for i in range(1, n + 1) if n % i == 0 and i % 2 == 0]
        array = np.array(even_factors)

        print("Even factors:", even_factors)
        print("NumPy array:", array)

# handle invalid input 
except ValueError:
    print("Please enter a valid integer.")