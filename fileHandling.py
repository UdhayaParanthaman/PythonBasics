import os
print(os.getcwd())

filetr=open("sample.txt","r")
print(filetr)
print("file is opened successfully")

filetr.close()  # closes the opened file