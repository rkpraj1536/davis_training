# Question 14: Data Cleaning Tool

clean_data = []

with open("messy_data.txt", "r") as file:
    for line in file:
        values = line.strip().split(",")

        try:
            cleaned = [value.strip() for value in values if value.strip() != ""]
            clean_data.append(cleaned)
        except Exception:
            print("Invalid Data")

print(clean_data)
