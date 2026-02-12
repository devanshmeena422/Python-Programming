s = {45,25,63,48,88}

print(s,type(s))
# print(s[3])  # You cant do something like this
s.add(26)
s.add(54)
s.add(20)
print(s)

s.remove(26)
s.remove(45)
print(s)

# s.remove(45454)
s.discard(54523)

s.pop()
print(s)