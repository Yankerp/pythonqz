# -*- coding utf-8 -*-

"""
@author:yankerp
@url:www.yankerphub.com
"""


# 一、有名函数
# func = 函数的内存地址
# def func(x, y):
#     return x + y


# 二、kambda定义匿名函数
# print(lambda x, y:x+y)  # <function <lambda> at 0x7f8f3e4d3700>

# 3、如何调用匿名函数
# 方式一：
# res = (lambda x, y:x+y)(1, 2)
# print(res)

# 方式二：
# func = lambda x, y:x+y
# res = func(1, 2)
# print(res)

"""以上的方式都不是匿名函数的调用场景"""

# 匿名函数用于临时调用一次的场景：更多的是将匿名函数与其他函数配合使用的场景
lambda x, y:x+y











