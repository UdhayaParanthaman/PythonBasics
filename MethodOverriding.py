class Laptop:
    def basicPrice(self):
        print("30k")
class Asus(Laptop):  # inherit parent class method is defined in child class with some specific implementation
    def basicPrice(self):
        print("Asus basic price: 35K")
class Dell(Laptop):
    def basicPrice(self):
        print("Dell Basic price :40k")

lap=Laptop()
lap.basicPrice()
asus=Asus()
asus.basicPrice()
