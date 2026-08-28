'''4. Add a static method in problem 2, to greet the user with helo.'''

class Calculator:
    def __init__(self, n):
        self.n = n

    def square(self):
        print(f"This Square is {self.n*self.n}")

    def cube(self):
        print(f"This Cube is {self.n*self.n*self.n}")

    def square_root(self):
        print(f"This is the Square Root {self.n**(1/2)}")

    @staticmethod
    def hello():
        print("Hello there!")

a = int(input("Enter the No."))
a = Calculator(a)
a.hello()
a.square()
a.cube()
a.square_root()










