def even_last(lst):
    new_lst = []
    for i in range(0,len(lst) , 2):
        new_lst.append(lst[i])
    return sum(new_lst)*lst[-1]

res = even_last([1, 3, 3, 1, 10])
print(res)