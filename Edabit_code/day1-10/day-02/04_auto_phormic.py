import math
def automorphic(n):
    squNum = int(math.pow(n , 2))
    i = len(str(n))
    num = ''
    while i !=0 :
        j = squNum%10
        num = str(j)+num
        squNum = int(squNum/10)
        i -= 1
    return int(num) == n


res = automorphic(25)
print(res)