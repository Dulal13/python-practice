def divisible_by_b(a, b):

    while True:
        
        a += 1
        if(a%b == 0):
            return a
        

res = divisible_by_b(14,11)
print(res)