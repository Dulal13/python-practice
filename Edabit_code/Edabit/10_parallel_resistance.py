def parallel_resistance(lst):
    res = 0
    for item in lst:
        res += (1/item)
    return round((1/res),1)
    
a = parallel_resistance([500,500,500])
print(a)