# -*- coding utf-8 -*-

"""
@author:yankerp
@url:www.yankerphub.com
"""


# 偷梁换柱即，将原函数名指向的内存地址偷梁换柱成wrapper的内存地址
# 所以应该将wrapper做的要和原函数一样才可以
from functools import wraps

def outter(func):

    @wraps(func)  # wraps这个就是一个装饰器，将func函数的属性赋值给wrapper函数解决了手动定义__name__ __doc__等等
    def wrappper(*args, **kwargs):
        "扩展功能"

        res = func(*args, **kwargs)  # 这是我的调用方式
        "扩展功能"
        return res
    # 将原函数的属性赋值给wrapper
    # wapper.__name__ = func.__name__
    # wapper.__doc__ = func.__doc__
    return wrappper


@outter  # index = outter(index)  得到wapper返回值，应该将wrapper做的和原函数一样才可以。
def index(a, b):
    """this is a  index func"""
    print(a + b)

# 目前以上的代码还是不够一样，还是有些地方不一样的。
# index(1, 2)
# print(index) # 此时的index就是wrapper：<function outter.<locals>.wapper at 0x7f7b334d3a60>
print(index.__name__)
print(index.__doc__)


