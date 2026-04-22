# Question 2: Fraud Transaction Detector

transactions = [
    {"user": "A", "amount": 1000, "time": 1},
    {"user": "A", "amount": 9000, "time": 2},
    {"user": "B", "amount": 200, "time": 5}
]

threshold = 5000
flagged = {}

for transaction in transactions:
    user = transaction["user"]

    if transaction["amount"] > threshold:
        flagged[user] = "High Amount"

print(flagged)
