# Write a program to find the sum of first n natural numbers using while loop.

n = int(input("Enter the number:-"))
i = 1
total = 0

while i < n+1: #i <= n:
    total = total + i
    i = i + 1

print(total)


