# Question 7: File Word Frequency Analyzer

stop_words = {"the", "is", "a", "an", "of", "and"}
frequency = {}

with open("article.txt", "r") as file:
    for word in file.read().lower().split():
        if word not in stop_words:
            frequency[word] = frequency.get(word, 0) + 1

top_words = list(frequency.items())
top_words.sort(key=lambda x: x[1], reverse=True)

print(top_words[:10])
