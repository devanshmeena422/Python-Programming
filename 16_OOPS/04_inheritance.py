class Animal: #parent class (superclass)
    location = "Australia"
    def __init__(self , name):
        self.name = name 
    def speak(self):
        print("speaking now ... ")

class Dog(Animal):  # This is how inheritance is done in python
    def speak(self):
        super().speak() # We are using the speak function of the parent class
        print("Woof !")

# a = Animal("Dog")
# a.speak()
d = Dog("bruno")
d.speak()
print(d.location)