def collatz(num):
    i = 0 
    while num!=1:
        if(num%2 == 0):
             num = num//2
             i += 1
        else:
            num = num*3 + 1
            i += 1
    return i

res = collatz(10)
print(res)

