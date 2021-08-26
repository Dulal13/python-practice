import random

randNo = random.randint(1,3)
if(randNo == 1):
    comp = 's'
elif(randNo == 2):
    comp = 'w'
elif(randNo == 3):
    comp = 'g'

def game(comp,you):

    if(comp == you):
        return None
    elif(you == 's'):
        if(comp =='w'):
            return True
        elif(comp == "g"):
            return False
    elif(you == "w"):
        if(comp =='s'):
            return False
        elif(comp == "g"):
            return True
    elif(you == 'g'):
        if(comp =='w'):
            return False
        elif(comp == "s"):
            return True


print('Computer turn:Snake(s) , Water(w) , Gun( g) : ')
you = input("Your turn :Snake(s) , Water(w) , Gun( g) :  ")
print(comp,you)
res = game(comp,you)

if(res == None):
    print('The match is tie')
elif(res == True):
    print('You win')
else:
    print('You lose')