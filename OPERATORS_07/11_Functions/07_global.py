def sum(a,b):
    print("that's all about global variable")
    c = a +b
    global z # please modify globAL Z
    z = 0   # this will refer to global Z and not create a local variable
    return c

z=5
print(sum(2,5))
print(z)