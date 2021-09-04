class Employee : 
    salary = 12

    @classmethod
    def changeSalary(cls , sal):
        cls.salary = sal

e = Employee()
print(e.salary)
e.changeSalary(45)
print(e.salary)
print(Employee.salary)


