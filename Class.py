class Employee:

    def empstatus(id,name):
        return id , name
res=Employee.empstatus(id=1,name="Udhaya")
print(res)




class Point:
    def move(self):
        print("Move")
    def draw(self):
        print('Draw')

point1=Point()  # creating object  (point1) for Point class
point1.x=8
point1.draw()
print(point1.x)
del point1      # deleting the Object to point class
# point1.move()



point2=Point()  # creating object (point2) for Point class
point2.x=9
print(point2.x)