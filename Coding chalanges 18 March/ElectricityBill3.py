# Electricity simple slab
u = int(input("Enter units: "))
#checking if bill amount is less than equal to 50
if u <= 50:
    bill = u * 1
else:
    bill = 50 * 1 + (u - 50) * 2
print("Bill:", bill)