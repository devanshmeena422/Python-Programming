class Employee:
    company = "HP"

    def __init__(self , name , salary):
        self.name = name
        self.salary = salary
    
    # @Instance Method (default) 
    def get_info(self):
        info =f"the name of the employe is {self.name} and his salary is {self.salary}"
        return (info)
    
    # Static Method
    @staticmethod
    def sum(a,b):
        return a + b
    
    # Class Method
    @classmethod
    def print_company(cls):
        print(cls.company)

 
    @classmethod
    def change_company(cls , new_company):
        cls.company = new_company


e1 = Employee("jack" , 50000)
e2 = Employee("john" , 60000)

print(Employee.company)
# print(Employee.name) This will throw an error


# print(e1.get_info())
# print(e2.get_info())

# print(e1.sum(15,52))
# print(e2.sum(15,85))

print(e1.print_company())
# print(e2.print_company())

e1.change_company("Acer")
e1.print_company()
print(Employee.company)