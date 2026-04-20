# Even numbers using while condition
n = int(input("Enter N: "))
i = 1
while i <= n:
    if i % 2 == 0:
        print(i, end=" ")
    i += 1