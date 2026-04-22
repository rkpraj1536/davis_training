# Question 4: Remove Duplicate Lines

unique_lines = []

with open("input.txt", "r") as input_file:
    for line in input_file:
        if line not in unique_lines:
            unique_lines.append(line)

with open("unique_lines.txt", "w") as output_file:
    for line in unique_lines:
        output_file.write(line)

print("Duplicate lines removed successfully")
