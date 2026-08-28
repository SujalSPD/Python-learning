# 1. Create a class (2-D vector) and use it to create another class representing a 3-D vector.

class TwoDVector:
    def __init__(self, i, j):
        self.i = i
        self.j = j

    def show(self):
        print(f"The 2D vector is {self.i}i + {self.j}j")


class ThreeDVector(TwoDVector):
    def __init__(self, i, j, k):
        super().__init__(i, j)
        self.k = k

    def show(self):
        print(f"The 3D Vector is {self.i}i + {self.j}j + {self.k}k")


a = TwoDVector(3,5)
a.show()
b = ThreeDVector(32,45,3)
b.show()




