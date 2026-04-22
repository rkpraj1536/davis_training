# Question 10: Email Extractor & Validator

import re

with open("data.txt", "r") as file:
    content = file.read()

emails = set(re.findall(r"[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}", content))

for email in emails:
    print(email)
