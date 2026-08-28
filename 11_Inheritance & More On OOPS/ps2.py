'''2. Create a class ‘Petsʼ from a class ‘Animalsʼ and further create a class ‘Dogʼ from ‘Petsʼ.
Add a method ‘barkʼ to class ‘Dogʼ.'''


class Animals:
    pass

class Pets(Animals):
    pass

class Dog(Pets):
    @staticmethod
    def bark():
        print("Bow Bow")


d = Dog

d.bark() 
