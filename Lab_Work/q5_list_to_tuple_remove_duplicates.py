# Question 5: Convert List to Tuple and Remove Duplicates

numbers = [1, 2, 2, 3, 4, 4]
unique_numbers = []

for element in numbers:
    if element not in unique_numbers:
        unique_numbers.append(element)

result_tuple = tuple(unique_numbers)

print("Tuple:", result_tuple)
