# Question 11: Remove Empty Sets from List

set_list = [{1, 2}, set(), {3, 4}, set()]
updated_list = []

for current_set in set_list:
    if len(current_set) > 0:
        updated_list.append(current_set)

print("Updated List:", updated_list)
