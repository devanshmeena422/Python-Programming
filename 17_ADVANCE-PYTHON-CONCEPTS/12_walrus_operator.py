def very_slow_func():
    print("Something...")
    print("Something...")
    print("Something...")
    print("Something...")
    print("Something...")
    print("Something...")
    return 7


# a = very_slow_func
if((a:=very_slow_func())): 
    print(a)

else:
    print("Its not greater than  10")