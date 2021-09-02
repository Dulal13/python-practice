def binary_to_decimal(lst):
    lst = int(''.join(list(map(lambda x:str(x) , lst))) , 2)
    return lst


res = binary_to_decimal([0, 0, 0, 1,1])
print(res)