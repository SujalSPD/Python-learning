# 2. Write a class “Calculator” capable of finding square, cube and square root of a number.

class Calculator:
    def __init__(self, n):
        self.n = n

    def square(self):
        print(f"This Square is {self.n*self.n}")

    def cube(self):
        print(f"This Cube is {self.n*self.n*self.n}")

    def square_root(self):
        print(f"This is the Square Root {self.n**(1/2)}")

a = int(input("Enter the No."))
a = Calculator(a)
a.square()
a.cube()
a.square_root()

