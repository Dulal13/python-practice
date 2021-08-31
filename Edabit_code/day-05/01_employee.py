class Employee:
    def __init__(self, firstname, lastname):
        self.firstname = firstname
        self.lastname = lastname
    def fullname(self):
        return "{} {}".format(self.firstname , self.lastname)
    def email(self):
        return "{}.{}@company.com".format(self.firstname.lower() , self.lastname.lower())

emp_1 = Employee("John", "Smith")
print(emp_1.fullname())
print(emp_1.email())
