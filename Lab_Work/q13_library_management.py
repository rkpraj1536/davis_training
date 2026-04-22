# Question 13: Library Management System

books = {"Python": True, "Java": True}

while True:
    choice = input("1.Issue 2.Return 3.Exit: ")

    if choice == "1":
        book = input("Book Name: ")
        if books.get(book):
            books[book] = False
            print("Book Issued")
        else:
            print("Not Available")

    elif choice == "2":
        book = input("Book Name: ")
        books[book] = True
        print("Book Returned")

    elif choice == "3":
        break

with open("library.txt", "w") as file:
    file.write(str(books))
