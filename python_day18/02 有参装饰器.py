# -*- coding utf-8 -*-

"""
@author:yankerp
@url:www.yankerphub.com
"""

# 一、知识储备
# 由于语法糖@的限制，outter函数只能有一个参数用来接收被装饰对象的内存地址
# def outter(func):
#     # func = 被装饰对象函数的内存地址
#     def wrapper(*args, **kwargs):
#         res = func(*args, **kwargs)
#         return res
#
#     return wrapper


"""
index参数是什么样子wrapper的参数就应该是什么样子
index的返回值是什么样子wrapper的返回值就是什么样子
index属性是什么样子。wrapper的属性就是什么样子 frok funtools import xxxx
"""

# 二、有参装饰器实现

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




















