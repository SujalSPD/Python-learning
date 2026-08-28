# 3. Create a class with a class attribute a; create an object from it and set ‘aʼ directly using
# ‘object.a = 0ʼ. Does this change the class attribute?

class Demo:
    a = 4

o = Demo()
print(o.a) # PRints the class attribute because instance attribute is not present
o.a = 0 # Instance attribute is set

print(o.a) # Prints the instance attribute because instance attribut is present
print(Demo.a) # Prints the calss attributs


