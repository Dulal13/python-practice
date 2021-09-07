def total_overs(balls):
    over_1 = balls//6
    over_2 = (balls%6)*.1
    
    return over_1+over_2

res = total_overs(164)
print(res)