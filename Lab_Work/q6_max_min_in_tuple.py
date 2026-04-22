# Question 6: Find Maximum and Minimum in Tuple

numbers_tuple = (5, 1, 8, 3)

maximum_value = numbers_tuple[0]
minimum_value = numbers_tuple[0]

for element in numbers_tuple:
    if element > maximum_value:
        maximum_value = element

    if element < minimum_value:
        minimum_value = element

print("Max =", maximum_value)
print("Min =", minimum_value)
