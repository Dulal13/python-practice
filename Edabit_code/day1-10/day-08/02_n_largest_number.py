def largest_numbers(n, lst):
    lst = sorted(lst)
    if n == 0:
        return []
    return lst[-1*n:]

res = largest_numbers(3, [14, 12, 57, 11, 18, 16]) 
print(res)