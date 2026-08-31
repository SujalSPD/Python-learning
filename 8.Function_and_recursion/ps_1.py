# Write a program using functions to find greatest of threee numbers.

def greatest(n1,n2,n3):
    if(n1>n2 and n1>n3):
        return n1
    elif(n2>n1 and n2>n3):
        return n2
    else:
        return n3

n1=1
n2=2
n3=3

print(greatest(n1,n2,n3))

    
