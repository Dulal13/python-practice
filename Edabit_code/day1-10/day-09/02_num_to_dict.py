def num_to_dict(lst):
    char = [str(chr(num)) for num in lst]
    dic = []
    for i in range(0 , len(lst)):
        dic.append(dict(zip([lst[i]] , char[i])))
    return dic

res = num_to_dict([118, 117, 120])
print(res)

