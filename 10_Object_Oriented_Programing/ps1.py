'''1. Create a class “Programmer” for storing information of few programmers working at
Microsoft.'''

class Programmer:
    def __init__(self, name, salary, role, looks):
        self.name=name
        self.salary=salary
        self.role=role
        self.looks=looks

    def show_info(self):
        print("Name:", self.name)
        print("Salary:", self.salary)
        print("Role:", self.role)
        print("Looks", self.looks)



Cometoze = Programmer("Cometoze", 50000 ,"Data Scientist", "Hot and Curvy")

Mia_Khalifa = Programmer("Mia_Khalifa", 50000 ,"Blow Job Engineer", "Busty and Sexy")

Scarlet_Johansonn = Programmer("Scarlet_Johansonn", 50000 ,"Gooning Engineer", "Super_Female_Body")

Cometoze.show_info()
print()

Mia_Khalifa.show_info()
print()

Scarlet_Johansonn.show_info()
print()

