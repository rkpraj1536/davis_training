# Question 9: Find Longest Line

with open("input.txt", "r") as input_file:
    longest_line = ""

    for line in input_file:
        if len(line) > len(longest_line):
            longest_line = line

print("Longest Line:")
print(longest_line)
print("Length:", len(longest_line))
