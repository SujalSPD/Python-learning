'''5. Store the multiplication tables generated in problem 3 in a file named Tables.txt .
'''
n = int(input("Enter a Number: "))

table = [n*i for i in range(1, 11)]
print(table)
with open("Tables.txt","a") as f:
    f.write(f"Table of {n}: {str(table)} \n")


