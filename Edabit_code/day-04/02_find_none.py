def find_none(lst):
    try:
         return lst.index(None)
    except:
        return -1
   

res = find_none([1,2,3,None])
print(res)