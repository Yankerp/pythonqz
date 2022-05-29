# -*- coding utf-8 -*-

"""
@author:yankerp
@url:www.yankerphub.com
"""

x = 111

def func():
    global x
    x = 2222222
    print(x)



# nonlocal(了解)
def func1():
    name = 'yanzan'
    def func2():
        nonlocal name
        name = 'zhangsan'
        print(name)
    func2()
    print('this is a func1>>>', name)

func1()
