# Program to calculate simple interest

p = float(input("Enter Principal: "))  # principal
r = float(input("Enter Rate: "))       # rate
t = float(input("Enter Time: "))       # time

si = (p * r * t) / 100   # formula for calculate simple interest

print("Simple Interest:", si)