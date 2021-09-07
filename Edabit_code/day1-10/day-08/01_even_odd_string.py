def even_odd_string(txt):
    even = ''
    odd = ''
    for i in range(0,len(txt)):
        if(i%2 == 0):
            even += txt[i]
        else:
            odd += txt[i]
    return "{} {}".format(even , odd)