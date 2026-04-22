# Question 8: Keyword Search Tool

keyword = input("Enter keyword to search: ").lower()

with open("input.txt", "r") as input_file:
    found = False

    for line in input_file:
        if keyword in line.lower():
            print(line.strip())
            found = True

    if not found:
        print("Keyword not found")
