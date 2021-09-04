def greet_people(names):
    
    greeting = ''
    for name in names:
        greeting +='Hello{},'.format(name)
    return greeting[:-1]