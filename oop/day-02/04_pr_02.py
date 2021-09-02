import math
class Calculator:

    def __init__(self,number):

        self.number = number

    def square(self):
        print(f"The square of the number is {math.pow(self.number,2)}")
        

    def cube(self):
         print(f"The cube of the number is {math.pow(self.number,3)}")

    def squareRoot(self):
         print(f"The squareRoot of the number is {round(math.sqrt(self.number),2)}")


a = Calculator(6)
a.square()
a.cube()
a.squareRoot()