# Question 4: Tuple Element Frequency

numbers_tuple = (1, 2, 2, 3, 1, 4)
frequency_dictionary = {}

for element in numbers_tuple:
    if element in frequency_dictionary:
        frequency_dictionary[element] += 1
    else:
        frequency_dictionary[element] = 1

print("Frequency:", frequency_dictionary)
