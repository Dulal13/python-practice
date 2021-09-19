def is_boiling(temp):
    tp = int(temp[0:-1])
   
    if(temp[-1] == "F"):
        if(tp>=212):
            return True
        else:
            return False
    elif(temp[-1] == "C"):
        if(tp>=100):
            return True
        else:
            return False

   

res = is_boiling("100C")
print(res)