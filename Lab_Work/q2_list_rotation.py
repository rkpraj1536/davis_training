# Question 2: List Rotation

numbers = [10, 20, 30, 40, 50]
k = 2

if len(numbers) > 0:
    k = k % len(numbers)
    rotated_list = numbers[-k:] + numbers[:-k]
    print("Rotated List:", rotated_list)
else:
    print("List is empty")
