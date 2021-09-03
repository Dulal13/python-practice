def is_harshad(n):
    n_sum = sum([int(x) for x in str(n)])
    return n%n_sum == 0