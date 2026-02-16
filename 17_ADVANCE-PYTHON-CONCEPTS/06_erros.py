# while True:
#     try:
#         a = int(input("enter first number :"))
#         b = int(input("enter second number : "))
#         print(f"the sum  of the numbers is : {a+b}")
#     except Exception as e:
        # print("some error occured!",e)


while True:
    try:
        a = int(input("enter first number :"))
        b = int(input("enter second number : "))
        print(f"the division  of the numbers is : {a/b}")

        if b == 0:
            raise ValueError("please dint perform this kind of mistakes")


    except ValueError:
        print("bad calcualtions")

    except ZeroDivisionError:
        print("value is not approachable")
    
    except Exception as e:
        print("some error occured!",e)
