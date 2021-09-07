def odd_sum_list(lst):
    condition = []

    for i in range(0 , len(lst) - 1):

        if((lst[i] + lst[i+1])%2 == 0):
            condition.append(True)
        else:
            condition.append(False)
    return condition