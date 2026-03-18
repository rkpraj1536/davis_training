# Program to calculate discount using separate variable

price = float(input("Enter price: ")) # input price
discount = float(input("Enter discount (%): "))

discount_amount = price * discount / 100   # calculate discount
final = price - discount_amount            # subtract discount
#print the final price
print("Final price:", final)