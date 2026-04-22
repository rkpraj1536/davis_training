# Question 9: Inventory Management System

inventory = {}

while True:
    choice = input("1.Add 2.Update 3.Delete 4.Exit: ")

    if choice == "1":
        item = input("Item name: ")
        quantity = int(input("Quantity: "))
        inventory[item] = quantity

    elif choice == "2":
        item = input("Item to update: ")
        quantity = int(input("New Quantity: "))
        inventory[item] = quantity

    elif choice == "3":
        item = input("Item to delete: ")
        inventory.pop(item, None)

    elif choice == "4":
        break

with open("inventory.txt", "w") as file:
    file.write(str(inventory))
