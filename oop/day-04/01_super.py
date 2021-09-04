class Game:
    km = 12
    def movement(self):
        print(f'Movement is {self.km}')

class Car(Game):
    num = 45
    def score(self):
        super().movement()
        print(f'Total score is : {self.num}')

c = Car()
c.score()
