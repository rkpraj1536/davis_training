# Question 7: Reverse File Content

with open("input.txt", "r") as input_file:
    file_lines = input_file.readlines()

reversed_lines = file_lines[::-1]

with open("reversed_output.txt", "w") as output_file:
    for line in reversed_lines:
        output_file.write(line)

print("File content reversed successfully")
