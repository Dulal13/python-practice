def single_occurrence(txt):
    txt = txt.upper()

    for char in txt:
        if(txt.count(char) == 1):
            return char
    else:
        return ''

res = single_occurrence("AAAAVNNNNSS")
print(res)