# Question 15: Palindrome Sentence Analyzer

sentence = input("Enter sentence: ").lower().split()
frequency = {}

for word in sentence:
    cleaned = word.replace(" ", "")

    if cleaned == cleaned[::-1]:
        frequency[cleaned] = frequency.get(cleaned, 0) + 1

print(frequency)
