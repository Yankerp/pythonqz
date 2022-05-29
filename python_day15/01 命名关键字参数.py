# -*- coding utf-8 -*-

"""
@author:yankerp
@url:www.yankerphub.com
"""

# 1、命名关键字参数（了解）
# 在定义函数的时候，*后定义的参数，如下所示,称之为命名关键字参数
#      特点：
# 1、命名关键字实参必须按照key=value的形式为其传值
def func(x,y, *, a, b): # 其中a和b称之为命名关键字参数
    print(x, y)
    print(a, b)