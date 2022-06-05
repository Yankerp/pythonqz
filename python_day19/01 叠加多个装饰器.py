# -*- coding utf-8 -*-

"""
@author:yankerp
@url:www.yankerphub.com
"""


def outter1(func):
    def wrapper1(*args, **kwargs):   # _func -------> wrapper2
        print("这是装饰器wrapper1开始运行作用...........")
        func(*args, **kwargs)

    return wrapper1


def outter2(func):
    def wrapper2(*args, **kwargs):  # _func -------> wrapper3
        print("这是装饰器wrapper2开始运行作用...........")
        func(*args, **kwargs)

    return wrapper2


def youcan(name):
    def outter(func):
        def wrapper3(*args, **kwargs):  # func -------->index
            print("这是装饰器wrapper3开始运行作用...........")
            func(*args, **kwargs)

        return wrapper3

    return outter


@outter1 # index = outter1(wrapper2) -----> index = wrapper1
@outter2 # index = outter2(wrapper3) ------> index = wrappper2
@youcan('yanzan') #@youcan('yanzan') ---> index = outter(index) -----> index ---> wrapper3
def index(x, y):
    print("this is a index >>>>>> ", x + y)


index(1, 2)
