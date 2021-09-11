def spin_around(lst):
    rotation = 0
    if lst[0] == "right":
        
        for item in lst:
            if item=="right":
                rotation += 90
            else:
                rotation -= 90
    elif(lst[0] == "left"):
        
        for item in lst:
            if item=="left":
                rotation += 90
            else:
                rotation -= 90
    else:
        return 0
    return abs(rotation)//360

res = spin_around(["left", "right", "left", "right"])
print(res)
