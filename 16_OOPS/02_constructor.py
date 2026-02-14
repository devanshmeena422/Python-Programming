class Employee :
    def __init__(self,salary,name,bond):
        self.salary = salary
        self.name = name
        self.bond = bond

    # def get_salary(self):
    #     return self.salary
    
    def get_info(self):
      print(f"the name of the employee is {self.name}. His salary is {self.salary}. He is in the company for {self.bond} years.")
e1 = Employee(34000,"john joe",5)
e1.get_info()
