'''4. Write a program to filter a list of numbers which are divisible by 5.'''
def divisible5(n):
    if(n%5 == 0):
        return True
    return False

a = [1,2,543,56343,342,544654,656,4555,65,555,6785,215]

f = list(filter(divisible5, a))
print(f)

