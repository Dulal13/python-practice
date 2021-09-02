class Programmer : 

    def __init__(self , name , company):
        self.name = name
        self.company = company

    def getDetails(self):
        print(f'The employee name is {self.name} and company name is {self.company}')

dulal = Programmer('Dulal' , 'Google')
hasib = Programmer('Hasib' , 'Youtube')

dulal.getDetails()
hasib.getDetails()