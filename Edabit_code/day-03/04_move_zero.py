def move_zeros(lst):
    lst1 = []
    for num in lst:
        if num == 0:
            lst.remove(num)
            lst1.append(int(num))
    return lst+lst1

res = move_zeros([9,0.0,0,9,1,2,0,1,0,1,0.0,3,0,1,9,0,0,0,0,9])
print(res)