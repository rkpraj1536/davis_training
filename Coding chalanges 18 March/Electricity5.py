# Electricity alternate slab
u = int(input("Enter units: "))
if u <= 100:
    print(u * 2)
else:
    print(100 * 2 + (u - 100) * 3)