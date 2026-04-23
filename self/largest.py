# Find largest number
nums = [10, 45, 23, 89, 12]
largest = nums[0]

for n in nums:
    if n > largest:
        largest = n

print("Largest:", largest)
