# Search word in file
key = input("Word: ")

with open("sample.txt", "r") as f:
    for line in f:
        if key in line:
            print(line.strip())
