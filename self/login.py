# Simple login system
user = input("Username: ")
pwd = input("Password: ")

if user == "admin" and pwd == "1234":
    print("Login successful")
else:
    print("Invalid credentials")
