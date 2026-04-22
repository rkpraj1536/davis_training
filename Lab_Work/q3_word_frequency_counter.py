# Question 3: Word Frequency Counter

import string

word_frequency = {}

with open("article.txt", "r") as article_file:
    content = article_file.read().lower()

for symbol in string.punctuation:
    content = content.replace(symbol, "")

words = content.split()

for word in words:
    if word in word_frequency:
        word_frequency[word] += 1
    else:
        word_frequency[word] = 1

print("Word Frequencies:")
for word, frequency in word_frequency.items():
    print(word, ":", frequency)
