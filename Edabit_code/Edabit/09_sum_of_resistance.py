def series_resistance(lst):
    all = sum(lst)
    if(all > 1):
        return "{total} ohms".format(total = all)
    else:
        return "{total} ohm".format(total = all)

res = series_resistance([1,2,3])
print(res)