import math
def count_digits(n, d):
    lst = []

    for i in range(n+1):
        lst.append(int(math.pow(i,2)))

    lst = list(map(lambda x:str(x) , lst))
    num_str = "".join(lst)
    
    return num_str.count(str(d))

res = count_digits(25,2)
print(res)