# Question 10: Compare Two Files

with open("file1.txt", "r") as first_file:
    file1_lines = first_file.readlines()

with open("file2.txt", "r") as second_file:
    file2_lines = second_file.readlines()

print("Lines present in file1 but not in file2:")

for line in file1_lines:
    if line not in file2_lines:
        print(line.strip())
