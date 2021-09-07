def forbidden_letter(char, lst):
    return  all(char not in item for item in lst)

res = forbidden_letter('e', ['rinse', 'and', 'repeat'])
print(res)