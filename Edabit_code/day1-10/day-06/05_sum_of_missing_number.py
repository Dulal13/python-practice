def sum_missing_numbers(lst):

    high = max(lst)
    low = min(lst)
    missing_number_list = []

    for i in range(low , high+1):
        if i not in lst:
            missing_number_list.append(i)
            
    return sum(missing_number_list)

res = sum_missing_numbers([17, 16, 15, 10, 11, 12])
print(res)