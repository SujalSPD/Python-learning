#Write a python program using function to convert Celsius to Fahrenheit
def f_to_c(f):
    c = 5*(f-32)/9
    return c
    
f = int (input("Enter the Temperature in F: "))
c = f_to_c(f)
print(f"{round(c,2)}°C")
