def rotate_max_number(num):
    num = sorted(list(map(lambda x:int(x),list(str(num)))))
    num.reverse()
    maxNum = ''
    for digit in num:
        maxNum += str(digit)
    print(maxNum)
res = rotate_max_number(765)