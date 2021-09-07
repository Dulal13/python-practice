def find_single_number(numbers):

    lst = []
    for number in numbers:
        if(numbers.count(number) == 1):
            lst.append(number)
    if(len(lst) >0):
        return lst[-1]
    else:
        return None

res = find_single_number([2, 2, 2, 3, 4, 4, 4])
print(res)
