def list_to_string(lst):
    lst = list(map(lambda x: str(x),lst))
    return ''.join(lst)

res = list_to_string([1, 2, 3, "a", "s", "dAAAA"]) 
print(res)