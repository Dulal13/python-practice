def list_between(num1, num2, lst):
    return list(filter(lambda x: x>num1 and x< num2 , lst))

res = list_between(3, 8, [1, 5, 95, 0, 4, 7])
print(res)