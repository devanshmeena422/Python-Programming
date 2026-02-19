import os

a = os.listdir("dir")
print(a)

print(os.getcwd()) # gives the current working directory

print(os.path.exists("sub")) # gives true/false if the directory is present or not

print(os.path.exists("devansh")) # gives true/false if the directory is present or not

# os.remove("delete.txt") # this will delete the file not the directory

os.rmdir('folder')
#This will only remove the empty directory