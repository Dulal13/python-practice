def upward_trend(lst):
    condition = True

    for i in range(0 , len(lst)-1):
        
        if (isinstance(lst[i] , int) and isinstance(lst[i+1] , int) ):
            if(lst[i] < lst[i+1]):
                condition = True
            else:
                return False
                break
        else:
            return "Strings not permitted!"
    return True


res = upward_trend([1, 2, 6,"h",  7, 8])
print(res)
