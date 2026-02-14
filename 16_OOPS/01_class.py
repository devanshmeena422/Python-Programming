# class : class is a blueprint or a template for an exam that contains name,age,electives,father's name etc

# Object : Specific instance created from the template (class). Eg.form which contain the data for john doe


class Employee:  # #self is a way to refernce the object of the class which is being created 
    company = "HP"

    def get_salary(self):  # Self is important here  becaucse is created here
        return 35000
    
e1 = Employee()     # An object of class employed 
print(e1.get_salary())   # Employed get salary method is called
print(e1.company)

e2 = Employee()
print(e2.get_salary() , e2.company)
