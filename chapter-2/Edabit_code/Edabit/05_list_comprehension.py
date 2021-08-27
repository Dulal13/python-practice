from typing import ItemsView


def one_list(lst):
    return [i for item in lst for i in item]

res = one_list([[1, 2], [3, 4],[8,7,9]])
print(res)

# [i for item in lst for i in item]
# [[1, 2], [3, 4]] ----> Item
# [1,2]----> i

