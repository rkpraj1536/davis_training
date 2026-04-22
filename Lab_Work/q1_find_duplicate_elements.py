# Question 1: Find Duplicate Elements in a List

numbers = [1, 2, 3, 2, 4, 5, 1]
duplicate_elements = []

for element in numbers:
    if numbers.count(element) > 1 and element not in duplicate_elements:
        duplicate_elements.append(element)

print("Duplicate Elements:", duplicate_elements)
