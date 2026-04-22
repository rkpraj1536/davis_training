# Question 17: Quiz System

score = 0

with open("questions.txt", "r") as file:
    for line in file:
        question, answer = line.strip().split(",")
        user_answer = input(question + " ")

        if user_answer.lower() == answer.lower():
            score += 1

print("Score:", score)
