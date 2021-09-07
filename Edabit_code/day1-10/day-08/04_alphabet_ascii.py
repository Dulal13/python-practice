def average_index(letters):
    ascii_value = list(map(lambda x: ord(x)-96 , letters))
    return round((sum(ascii_value)/len(letters)),2)

res = average_index(["a", "b", "c", "i"])
print(res)