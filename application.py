import random

for i in range(1):
    print(random.random())
#generate random number from 10 to 20
for i in range(5):
    print(random.randint(10,20))

#generate random Guy as teamlead
employee =['Udhaya','Manikandan','Saravanan','Sujan']
lead=random.choice(employee)
print(lead)