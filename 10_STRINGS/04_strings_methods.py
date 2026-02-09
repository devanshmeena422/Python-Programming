s = "Hello world" # strings are immutable

# name[0] = "R" # you cannot do this

a = len(s)
print(a)
print(s.upper())
print(s.lower())
print(s.capitalize())
print(s.title())


text = "\n   hello world  " 
print(text)
print(text.strip())
print(text.lstrip())
print(text.rstrip())
print("End OF PROGRAM\n")



print("NEXT\n")



text = "python is fun"
print(text)
print(text.find("is")) #its the index of first occurence output = 7
print(text.replace("fun","awesome"))
print("End OF PROGRAM\n")


print("NEXT\n")

text = "Apples,Bannanas,Pineapples"
print(text)
print(text.split((",")))
print(",".join(['Apples' ,'Bannanas', 'Pineapples']))
print("End OF PROGRAM\n")


print("NEXT\n")

text = "python123"
print(text.isalpha())
print(text.isdigit())
print(text.isalnum())
print(text.isspace())
print("End OF PROGRAM\n")

print("THANK YOU")
