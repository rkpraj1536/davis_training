# Question 6: File Merge with Line Numbers

with open("file1.txt", "r") as first_file:
    file1_lines = first_file.readlines()

with open("file2.txt", "r") as second_file:
    file2_lines = second_file.readlines()

merged_lines = file1_lines + file2_lines

with open("merged_file.txt", "w") as merged_file:
    line_number = 1

    for line in merged_lines:
        merged_file.write(f"{line_number}. {line}")
        line_number += 1

print("Files merged successfully")
