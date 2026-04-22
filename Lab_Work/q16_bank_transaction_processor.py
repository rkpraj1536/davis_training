# Question 16: Bank Transaction Processor

class OverdraftError(Exception):
    pass

balance = 0

with open("transactions.csv", "r") as file:
    for line in file:
        account, transaction_type, amount = line.strip().split(",")
        amount = float(amount)

        if transaction_type == "deposit":
            balance += amount
        elif transaction_type == "withdraw":
            if amount > balance:
                raise OverdraftError("Insufficient Balance")
            balance -= amount

print("Final Balance:", balance)
