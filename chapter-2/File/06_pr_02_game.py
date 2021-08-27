def game():
    return 89

you = game()

with open('score.txt') as f:
    if (f.read() == ''):
        with open('score.txt','w') as f:
            f.write(str(you))
    else:
        with open('score.txt') as f:
            if(int(f.read()) < you):
                 with open('score.txt','w') as f:
                     f.write(str(you))
