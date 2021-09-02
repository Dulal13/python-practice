def find_difference(a, b):
    
    a_vol = a[0]*a[1]*a[2]
    b_vol = b[0]*b[1]*b[2]
    
    return abs(a_vol-b_vol)
