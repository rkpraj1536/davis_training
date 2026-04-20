# Program to calculate electricity bill (step approach)

units = int(input("Enter units consumed: "))

bill = 0 #define bill initially 0
# checking if the units in range and calculte the per unit charge accordingly
if units > 100:
    bill = 100 * 1.5
    remaining = units - 100
    bill = bill + remaining * 2.5
else:
    bill = units * 1.5
# printing total bill generated
print("Total bill:", bill)