class Employee :
    company = "ASUS"
    def __init__(self,salary,name,bond,company):
        self.salary = salary
        self.name = name
        self.bond = bond
        self.company = company

    def get_salary(self):
        return self.salary
    
    def get_info(self):
      print(f"the name of the employee is {self.name}. His salary is {self.salary}. He is working in the {self.company} company for {self.bond} years.")
e1 = Employee(34000,"john joe",5,"TESLA")
e1.get_info()
print(e1.company)
print(Employee.company)
# print(class.Employee(company))

# OBJECT INTROSPECTION

print(dir(e1))  # THIS WILL PRINT THE ALL METHODS OF THE (e1) dir
