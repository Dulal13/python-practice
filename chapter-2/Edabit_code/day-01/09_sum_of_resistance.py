def series_resistance(lst):
    all = sum(lst)
    return "{total} ohms".format(total = all)

res = series_resistance([1,2,3])
print(res)