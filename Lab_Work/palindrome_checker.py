# 8. Palindrome Checker

def is_palindrome(value):
    value = str(value)
    reversed_value = ""

    for character in value:
        reversed_value = character + reversed_value

    return value == reversed_value

user_input = input("Enter a number or string: ")

if is_palindrome(user_input):
    print("It is a Palindrome")
else:
    print("It is Not a Palindrome")
