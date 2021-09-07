def journey_distance(n):
    if(n>3):
        n = n - 3
        return 1+n//2
    elif(n == 3):
        return 1
    else:
        return 0

res = journey_distance(9)
print(res)