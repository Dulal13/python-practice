def sum_list(lst):
    lst = [j for i in lst for j in i]
    print(lst)

res = sum_list([1, [2, [1]], 3])
print(res)
