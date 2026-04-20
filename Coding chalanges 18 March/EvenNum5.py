# Even numbers excluding zero
n = int(input("Enter N: "))
for i in range(n):
    if i % 2 == 0 and i != 0:
        print(i)