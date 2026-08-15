# Write a python function which converts inches to cms.

def inch_to_cm(inch):
    return inch * 2.54

n = int (input("Enter the lenght in Inches: "))

print(f"The corresponding value in cm is: {inch_to_cm(n)}cm")


