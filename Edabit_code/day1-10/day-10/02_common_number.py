def sum_common(lst1, lst2, lst3):

    common_list = []

    for item in lst1:

        if(item in lst2 and item in lst3):
            if item not in common_list:
                common_list.append(item)
    return sum(common_list)


