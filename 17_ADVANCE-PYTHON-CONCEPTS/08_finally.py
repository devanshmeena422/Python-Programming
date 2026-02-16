def divide(a,b):
    try:
        c = a/b
        print(c)
        return c

    except Exception as e:
        print(e)
        return None
    
    #This will always be executed no metter what try completes or not
    finally:
        print("this will always be executed")

a = int(input("enter first number :"))
b = int(input("enter second number : "))
divide(a,b)
