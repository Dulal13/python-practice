def find_bob(names):
    try:
        return names.index('Bob')
    except:
        return -1

res = find_bob(["Layla", "Kaitlyn", "Patricia"])
print(res)