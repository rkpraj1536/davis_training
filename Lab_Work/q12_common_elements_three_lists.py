# Question 12: Common Elements in Three Lists

list1 = [1, 2, 3]
list2 = [2, 3, 4]
list3 = [2, 5, 3]

common_elements = []

for element in list1:
    if element in list2 and element in list3:
        common_elements.append(element)

print("Common Elements:", common_elements)
