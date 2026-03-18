# taking price and discount price separetly
price = float(input("Enter price: "))
disc = float(input("Enter discount: "))
#calculate final price and print it along with it
print("Final:", price - price * disc / 100)