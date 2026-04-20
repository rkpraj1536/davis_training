# Electricity different slab
u = int(input("Enter units: "))
if u <= 200:
    bill = u * 2
else:
    bill = 200 * 2 + (u - 200) * 5
print(bill)