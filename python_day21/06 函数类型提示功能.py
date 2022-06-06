# -*- coding utf-8 -*-

"""
@author:yankerp
@url:www.yankerphub.com
"""


# python3.5之后的版本才支持这样的功能
def func(name: str, age: int, li: dict)->int:
    print(name, age, li)
    return 100

func('yanzan', 19, {'name': 'zhangsan'})
