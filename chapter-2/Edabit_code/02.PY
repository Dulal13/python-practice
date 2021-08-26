import math
def is_narcissistic(n):
    lst =list(map(lambda x:int(x), list(str(n))))
    product = 0
    for item in lst:
        product += math.pow(item , len(lst))
    return product == n


res = is_narcissistic(153)
print(res)