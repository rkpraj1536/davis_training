# Question 5: Sales Data Aggregator

sales = {}
highest_product = ""
highest_amount = 0

with open("sales.csv", "r") as file:
    for line in file:
        try:
            product, category, price, quantity = line.strip().split(",")
            total = float(price) * int(quantity)

            sales[category] = sales.get(category, 0) + total

            if total > highest_amount:
                highest_amount = total
                highest_product = product

        except ValueError:
            print("Invalid Row:", line.strip())

print("Sales Per Category:", sales)
print("Highest Selling Product:", highest_product)
