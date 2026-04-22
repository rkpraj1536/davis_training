# Question 13: Flatten Nested List

nested_list = [[1, 2], [3, 4], [5]]
flat_list = []

for sublist in nested_list:
    for element in sublist:
        flat_list.append(element)

print("Flattened List:", flat_list)
