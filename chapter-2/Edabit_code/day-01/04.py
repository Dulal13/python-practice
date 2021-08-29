def trimmed_averages(lst):
    lst = sorted(lst)
    lst.remove(lst[0])
    lst.remove(lst[-1])
    return round(sum(lst)/len(lst))
res = trimmed_averages([5,6,7,4])


# lst = [5,4,3,2,2]
# print(sorted(lst))