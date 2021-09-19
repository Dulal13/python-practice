def mumbling(s):
    i = 1
    sample =""
    for item in (list(s)):
        a = (item*i).capitalize() 
        sample += a+"-"
        i = i+1
    return sample[0:-1]

res = mumbling("Dulal")
print(res)
