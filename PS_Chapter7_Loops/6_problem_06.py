# Write a program to calculate the factorial of a given number using for loop.

n = int(input("Enter the number that you want to find the factorial:-"))
total = 1    
for i in range (1,n+1):
    total = total*i
    i = i +1

print(total)


