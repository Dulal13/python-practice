class Employee:
    basic_salary = 5699
    bonus = 1000

    @property
    def totalSalary(self):
        return self.basic_salary + self.bonus

e = Employee()
print(e.totalSalary)