# Question 15: Tuple to Dictionary Mapping

keys = ('a', 'b', 'c')
values = (1, 2, 3)

if len(keys) == len(values):
    result_dictionary = {}

    for index in range(len(keys)):
        result_dictionary[keys[index]] = values[index]

    print("Dictionary:", result_dictionary)
else:
    print("Error: Number of keys and values must be equal")
