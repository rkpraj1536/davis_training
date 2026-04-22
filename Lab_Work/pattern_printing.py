# 9. Pattern Printing with Conditions

rows = int(input("Enter number of rows: "))

if rows <= 0:
    print("Please enter a positive number")
else:
    for row in range(1, rows + 1):
        if row % 2 == 0:
            symbol = "*"
        else:
            symbol = "#"

        for column in range(row):
            print(symbol, end=" ")

        print()
