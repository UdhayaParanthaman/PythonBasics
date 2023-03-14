class Constructor:
    def __init__(self ,x,y): # initialize the constructor to current class with x,y parameter
        self.x=x
        self.y=y
    def move(self):
        print("move")
con =Constructor(10,27)
con.y=87 # y is updated
con.x=input()
print(con.x)
con.move()

class Person:

    def __init__(self,name,age):  # creating constructor to store attribute value
        self.name=name
        self.age=age

    def talk(self):
        print(f"Hii I am {self.name}")

person =Person("Udhaya Kumar",23)
person.talk()
print(getattr(person,'name'))  # getattribute from name object
setattr(person,"name","Udhaya") # set attribute to name=Udhaya
print(hasattr(person,"name")) # returns true if object is present
person.talk()


person1 =Person('Manikandan',24)
person1.talk()

# Non-parameterized constructor
class Laptop:
    def __init__(self):
        print("This is not parametrized constructor")

    def brand(self,name):
        print(name)
lap=Laptop()
lap.brand("Asus")
