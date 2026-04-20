# Voting using variable result
age = int(input("Enter age: "))
result = "Eligible"
#changing the variable later
if age < 18:
    result = "Not Eligible"
print(result)