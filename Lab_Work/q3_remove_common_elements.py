# Question 3: Remove Common Elements from Two Lists

list1 = [1, 2, 3, 4]
list2 = [3, 4, 5]

result_list = []

for element in list1:
    if element not in list2:
        result_list.append(element)

print("Updated List:", result_list)
