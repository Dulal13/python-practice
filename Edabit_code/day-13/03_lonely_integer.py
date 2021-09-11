def lonely_integer(lst):
    for number in lst:
        if number*-1 not in lst:
            return number