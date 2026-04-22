# Question 9: Merge and Sort Unique Elements

list1 = [3, 1, 2]
list2 = [2, 4, 5]

merged_list = list1 + list2
unique_elements = []

for element in merged_list:
    if element not in unique_elements:
        unique_elements.append(element)

unique_elements.sort()

print("Sorted Unique List:", unique_elements)
