# -*- coding utf-8 -*-

"""
@author:yankerp
@url:www.yankerphub.com
"""


# 函数嵌套：
# 1、函数的嵌套调用：在调用一个函数的过程中又调用其他的函数
def bar():
    pass


def foo():
    bar()


foo()
# 2、函数的嵌套定义：在函数内定义函数
def func():
    def func2():
        pass




