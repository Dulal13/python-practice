def add(char, txt):
    a = txt.split(" ")
    return char.join(a)

res = add("R", "python is fun")
print(res)