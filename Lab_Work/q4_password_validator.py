# Question 4: Custom Password Validator

class InvalidPasswordError(Exception):
    pass

password = input("Enter password: ")

try:
    if len(password) < 8:
        raise InvalidPasswordError("Minimum 8 characters required")

    if not any(ch.isupper() for ch in password):
        raise InvalidPasswordError("One uppercase letter required")

    if not any(ch.islower() for ch in password):
        raise InvalidPasswordError("One lowercase letter required")

    if not any(ch.isdigit() for ch in password):
        raise InvalidPasswordError("One digit required")

    print("Valid Password")

except InvalidPasswordError as error:
    print(error)
