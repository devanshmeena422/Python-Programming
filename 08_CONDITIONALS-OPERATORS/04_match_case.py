a = int(input("Enter number between 1 to 10 : "))

match a:
    case 1:
        print("you won a charger")
    case 3:
        print("you won $3")
    case 6:
        print("you won a camera")
    case _:
        print("better luck next time")