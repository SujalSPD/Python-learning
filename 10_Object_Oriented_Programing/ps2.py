# 2. Write a class “Calculator” capable of finding square, cube and square root of a number.
import math


class Calculator:
    def __init__(self, a):
        self.a = a

    def square(self):
        Square = (self.a*self.a)
        print(f"This is the Square {Square}")

    def cube(self):
        Cube = (self.a*self.a*self.a)
        print(f"This is the Cube {Cube}")

    def square_root(self):
        result = math.sqrt(self.a)
        print(f"This is the Square Root {result}")

a = int(input("Enter the No. which you want to find square, cube and square root:"))

calculator = Calculator(a)

calculator.square()
calculator.cube()
calculator.square_root()

