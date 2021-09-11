import math
def height(side):
    lengthOfHeight = math.sqrt(math.pow(side , 2)-math.pow(side/2 , 2))
    x = round(lengthOfHeight*10 , 1)
    return "{} mm".format(x)

res = height(5)
print(res)