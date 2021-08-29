import math
def radians_to_degrees(rad):
    return round(rad*(180/math.pi),1)

res = radians_to_degrees(1)
print(res)
