# Question 10: Tuple Pair Sum

numbers_tuple = (1, 2, 3, 4, 5)
target_sum = 5
pairs = []

for i in range(len(numbers_tuple)):
    for j in range(i + 1, len(numbers_tuple)):
        if numbers_tuple[i] + numbers_tuple[j] == target_sum:
            pairs.append((numbers_tuple[i], numbers_tuple[j]))

print("Pairs:", pairs)
