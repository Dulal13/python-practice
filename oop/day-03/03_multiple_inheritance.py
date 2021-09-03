class Employee : 
    company = 'Google'

class UpWork:
    company = 'esite'

class Programmer( UpWork , Employee):
    pass

p = Programmer()
print(p.company)