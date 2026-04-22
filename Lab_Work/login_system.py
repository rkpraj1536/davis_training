# 3. Login System (3 Attempts)

correct_username = "admin"
correct_password = "1234"

attempt = 1

while attempt <= 3:
    username = input("Enter Username: ")
    password = input("Enter Password: ")

    if username == correct_username and password == correct_password:
        print("Login Successful")
        break
    else:
        print("Invalid Username or Password")
        attempt += 1

if attempt > 3:
    print("Account Locked")
