def win_round(you, opp):
    you_num = sorted(you)[-2:]
    you_num.reverse()
    you_num = [str(x) for x in you_num]
    mark = int("".join(you_num))

    opp_num = sorted(opp)[-2:]
    opp_num.reverse()
    opp_num = [str(x) for x in opp_num]
    mark1 = int("".join(opp_num))

    return mark > mark1
    
    

res = win_round([2, 5, 2, 6, 9], [3, 7, 3, 1, 2])