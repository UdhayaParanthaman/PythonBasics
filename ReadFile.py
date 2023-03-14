
import os;
#deleting the file named file3.txt
# os.remove("pythonsample.txt")

newFile=open("python.txt",'r')

con=newFile.readline()
print(con)

newFile=open("sample.txt",'r')
content2=newFile.readlines()
print(content2)


