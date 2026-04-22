# Question 5: Email Extractor

import re

with open("data.txt", "r") as data_file:
    file_content = data_file.read()

email_list = re.findall(r"[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}", file_content)

with open("emails.txt", "w") as email_file:
    for email in email_list:
        email_file.write(email + "\n")

print("Emails extracted successfully")
