def asc_des_none(lst, s):
    
    if s=='Asc':
        return sorted(lst)
    elif s=='Des':
      return  sorted(lst , reverse=True)  
    else:
        return lst

res = asc_des_none([7, 8, 11, 66], "Des")
print(res)