# Count lines, words, characters
with open("sample.txt", "r") as file:
    content = file.read()
    print("Chars:", len(content))
    print("Words:", len(content.split()))
    print("Lines:", len(content.split("\n")))
