word = ['rakib' , 'tuhin' , 'Dulal']

with open('sample.txt') as f:
    data = f.read()
    
    for item in word:
        data = data.replace(item,'@#$')

with open('sample.txt' , 'w') as f:
    f.write(data)