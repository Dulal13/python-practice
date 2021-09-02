def is_equal(lst):

    a = sum([int(x) for x in str(lst[0])])
    b = sum([int(x) for x in str(lst[1])])

    return a == b
