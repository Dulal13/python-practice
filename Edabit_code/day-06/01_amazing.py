def amazing_edabit(s):
    if 'edabit' in s:
        return s
    else:
        s = s.replace('amazing' , 'not amazing')
        return s

res = amazing_edabit("edabi is amazing.")
print(res)