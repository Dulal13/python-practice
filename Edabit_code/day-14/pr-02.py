def imposter_formula(i, p):
    percentage = round((100*i)/p)
    return "{}%".format(percentage)


res = imposter_formula(3,7)
print(res)