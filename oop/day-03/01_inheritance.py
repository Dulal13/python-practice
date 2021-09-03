class Father:
    age = 43

   
    def company(self):
        print('The company name is Google')

class Son(Father):
    company = 'google'

    def ageOfFather(self):
        print(f"The age father is : {self.age}")
    def company(self):
        print(f'The company name is {self.company}')


dulal =  Son()
kalam = Father()

dulal.company()
kalam.company()