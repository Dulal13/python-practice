def parse_list(lst):
    return list(map(lambda x:str(x),lst))
    
res = parse_list([1, 2, "a", "b"])
print(type(res[0]))