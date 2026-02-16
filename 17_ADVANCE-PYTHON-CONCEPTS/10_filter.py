def is_greater_than_9(x):
    if x>9:
        return True
    else:
        return False

a1 = [3,5,9,90,89,6,79,54,23,1,54,6,7,4,5,4]

new = list(filter(is_greater_than_9, a1))
print(new)


# ANOTHER WAY OF DOING THIS

a2 = [3,5,8,9,89,56,34,2,1,45,7]
new2 = list(filter(lambda x: x>9 , a2))
print(new2)