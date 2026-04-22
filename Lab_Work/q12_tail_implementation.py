# Question 12: Tail Implementation (Like Linux tail)

number_of_lines = int(input("Enter number of last lines to display: "))

with open("input.txt", "r") as input_file:
    all_lines = input_file.readlines()

if number_of_lines <= 0:
    print("Please enter a positive number")
else:
    last_lines = all_lines[-number_of_lines:]

    print("Last", number_of_lines, "lines:")
    for line in last_lines:
        print(line.strip())
