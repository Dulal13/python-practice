import math
def next_square(n):

    squareRoot = round(math.sqrt(n) , 1)
    
    # print(squareRoot)
    if(squareRoot*squareRoot == n):
        return round(math.pow(squareRoot+1 , 2))
    else:
        return None

res = next_square(625)
print(res)
