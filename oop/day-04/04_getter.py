class Employee:
    basic_salary = 5699
    bonus = 1000

    @property
    def totalSalary(self):
        return self.basic_salary + self.bonus
    
    @totalSalary.setter
    def totalSalary(self , val):
        self.bonus = val - self.basic_salary


e = Employee()
print(e.totalSalary)
e.totalSalary = 6550
print(e.bonus)
