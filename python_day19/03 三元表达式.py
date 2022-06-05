# -*- coding utf-8 -*-

"""
@author:yankerp
@url:www.yankerphub.com
"""

# 三元表达式的语法:
#   条件成立时返回的值   if  条件  else  条件不成立时返回的值

# def func(x, y):
#     if x > y:
#         return x
#     else:
#         return y
#
# res = func(1, 3)
# print(res)

# x = 1
# y = 4
# res = x if x > y else y
# print(res)

def func2(x, y):
    res = x if x > y else y
    return res
es = x if x > y else y
# print(res)

def func2(x, y):
    res = x if x > y else y
    return res

res = func2(1, 9)
print(res)
res = func2(1, 9)
print(res)