def tuck_in(lst1, lst2):
    
    lst2.insert(0 , lst1[0])
    lst2.append(lst1[1])

    return lst2

res = tuck_in([[1, 2], [5, 6]], [[3, 4]]) 
print(res)