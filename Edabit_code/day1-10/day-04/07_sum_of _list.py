import math
def list_sum(lst):
    new_list = []

    for number in lst:
        if (number%2 == 0):
            new_list.append(math.pow(number,2))
        else:
            new_list.append(math.sqrt(number))
    return round(sum(new_list),2)

res = list_sum([1, 31, 3, 11, 0])
print(res)