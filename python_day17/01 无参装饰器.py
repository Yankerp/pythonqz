# -*- coding utf-8 -*-

"""
@author:yankerp
@url:www.yankerphub.com
"""

# 一、装饰器
"""
1、什么是装饰器？
    器指的就是工具，可以定义成函数
    装饰：指的是为其他事物添加功能，添加额外的东西来点缀（有些抽象哦）
    
    合到一起的解释：
        装饰器：指的是定义一个函数或类，但是该函数是用来装饰其他函数的，为其他函数添加额外的功能

2、为何要用装饰器？
    开放封闭原则
        开放：指的是对拓展功能是开放的
        封闭：指的是对修改源代码是封闭的

    结论：装饰器就是在不修改被装饰对象源代码以及调用方式的前提下为被装饰对象添加增加新的功能

3、如何定义装饰器？
"""

import time


def user_out(name, age, url):
    print(name, age, url)


# def resu(x):
#     def warrep(*args, **kwargs):
#         start = time.time()
#         time.sleep(2)
#         x(*args, **kwargs)
#         stop = time.time()
#         print(stop - start)
#
#     return warrep
#
#
# user_out = resu(user_out)

# 装饰器实现！
# user_out('yanzan', 19, 'beijing')

# user_out('yanzan', 19, 'beijing')


import time


def home(name):
    time.sleep(2)
    print('this is a home>>>', name)
    return 12311111

aaa = home('yanzan')
# 装饰器太简单了，学到目前为止