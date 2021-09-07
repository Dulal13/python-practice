def to_dict(lst):
    lst = sorted(lst)
    dic = []
    if len(lst) == 0:
        return []
    else:
        ascii_value = list(map(lambda x: ord(x) , lst))
        for i in range(0,len(lst)):
            dic.append (dict(zip([lst[i]] , [ascii_value[i]])))
    return dic

res = to_dict(['c' , 'a','b'])
print(res)