class Mammal:
    def walk(self):
        print("Walking")


class Dog(Mammal):   # Dog class inherits the mammal
    pass
class Cat(Mammal):  # Cat class inherits the mammal
    pass
dog =Dog()
dog.walk()
cat =Cat()
cat.walk()