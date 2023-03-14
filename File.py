from pathlib import Path

#Absolute path

#Relative path
path =Path("Ecommerce")
print(path.exists())
path1=Path('s')
print(path1.mkdir())  # make directive to email [creating the email directive]
print(path1.rmdir())    # remove the directive

path2=Path()
for file in path2.glob('*'): # has return all file in current package
    print(file)

