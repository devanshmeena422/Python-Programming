numbers = (2,4,6,8,10)

def square(x):
    return x ** 2

new_numbers = tuple(map(square , numbers))
print(new_numbers)