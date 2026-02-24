try:
    a = int(input("Enter first Number : "))
    b = int(input("Enter second Number : "))
    # operation = ('+' , '-' , '*' , '/')

    o = input('Enter the operation : ') 
    match o:
        case '+':
            print(f"The addition of both the numbers is : , {a+b}")
        case '-':
            print(f"The subtraction of both the numbers is : , {a-b}")
        case '*':
            print(f"The multiplication of both the numbers is : , {a*b}")
        case '/':
            print(f"The division of both the numbers is : , {a/b}")
        case default:
            print(f"There was an error")

except Exception as e:
    print("please enter vlaid value of a and b" , e)