#string formatting

template = "{} please stand up and bring me a {}"

a= "ram"
a1="chair"
b="shyam"
b1= "water bottle"
c= "suresh"
c1="umbrella"

s1=template.format(a,a1) # old way
print(s1)


print(f"{b} please stand up and bring me a {a1}")  #new way