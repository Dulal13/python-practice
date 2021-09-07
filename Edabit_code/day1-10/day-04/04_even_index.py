def even_last(lst):
    new_list = [lst[i] for i in range(0,len(lst),2)]
    return sum(new_list)*lst.pop()

res = even_last([-11, 3, 3, 1, 10])
print(res)