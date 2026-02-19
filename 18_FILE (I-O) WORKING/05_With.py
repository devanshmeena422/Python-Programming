# f = open('devansh.txt' , 'r')

# content = f.read()
# print(content)
# f.close 
## Its not neccesary to write f.close() without this the program will run but its a good coder manaers of writing f.close

with open('devansh.txt' , 'r') as f: # this is known as context manager
    content = f.read()
    print(content)

#No need to write f.close() because file is already closed by default when using with syntax