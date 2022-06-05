# -*- coding utf-8 -*-

"""
@author:yankerp
@url:www.yankerphub.com
"""

from functools import wraps


def youcan(namespace):
    def outter(func):
        @wraps(func)
        def zhuce(*args, **kwargs):
            your_name = input("输入登录名：").strip()
            your_pwd = input("输入登录密码：").strip()
            print("这是有参装饰器传来的参数：", namespace)
            if your_name == 'yanzan' and your_pwd == 'pwd123':
                res = func(*args, **kwargs)
                return res
            else:
                print("登录失败！！！")

        return zhuce
    return outter

@youcan(namespace='namespace')
# func1 = outter(func1)  func1此时得到了zhuce的内存地址.   so? func1(1, 2) == zhuce(1, 2)
def func1(x, y):
    "这是一个功能"
    print("欢迎来到澡堂", x, y)
    return 'ok'

# @youcan(namespace='namespace')
# youcan(namespace='namespace')--->得到一个返回值outter == @outter == func1 = outter(func1) == 得到zhuce内存地址  func1 = zhuce

@youcan(namespace='namespace')
# func2 = outter(func2)  func2此时得到了zhuce函数的内存地址.   func2(1, 2) == zhuce(1, 2)
def func2(x, y):
    "这是一个功能"
    print("欢迎来到课堂", x, y)


@youcan(namespace='namespace')
# func3 == outter(func3) func3此时得到了zhuce函数的内存地址。    func3(1,2) == zhuce(1, 2)
def func3(x, y):
    "这是一个功能"
    print("欢迎来到教堂", x, y)

func1(1, 3)