import math
def javelin_throw(v, a):
    b = 2*a
    r = (v*v*math.sin(b))/9.81
    h = (2*v*math.sin(a))/9.81
    return (r,h)

res = javelin_throw(36.7, 45)
print(res)
