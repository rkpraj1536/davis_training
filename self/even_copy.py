# Copy even numbers
with open("numbers.txt", "r") as f:
    nums = f.readlines()

with open("even.txt", "w") as out:
    for n in nums:
        n = int(n.strip())
        if n % 2 == 0:
            out.write(str(n) + "\n")
