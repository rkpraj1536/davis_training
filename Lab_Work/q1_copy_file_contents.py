# Question 1: Copy contents of one file into another

with open("source.txt", "r") as source_file:
    file_content = source_file.read()

with open("destination.txt", "w") as destination_file:
    destination_file.write(file_content)

print("File copied successfully")
