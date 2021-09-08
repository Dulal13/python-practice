def inclusive_list(start_num, end_num):
    if(start_num < end_num):
        return [x for x in range(start_num , end_num+1)]
    else:
        return [start_num]