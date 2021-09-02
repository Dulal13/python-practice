class Student:
    
    def __init__(self,name,age,company):

        self.name = name
        self.age = age
        self.company = company
    
    def getDetails(self):
        print({
            'name' : self.name,
            'age':self.age,
            'company' : self.company
        })
    @staticmethod
    def greet():
        print('Hi')

obj  = Student('Dulal',22,'Googler')
obj.getDetails()