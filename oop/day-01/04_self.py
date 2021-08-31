class Car:
    color = 'red'
    price = 1000

    def carFunc(self):
       return ({
            'outSide' : self.color,
            'cost' : self.price,
            'people' : self.sit
             })

dulalCar = Car()
dulalCar.sit = 5
res = dulalCar.carFunc()
print(res)