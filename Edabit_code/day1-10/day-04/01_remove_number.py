def remove_numbers(string):
    lst = list(string)
    return ''.join(i for i in lst if i.isalpha())

res = remove_numbers("mub67ashir1")
print(res)