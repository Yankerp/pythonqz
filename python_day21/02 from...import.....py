# -*- coding utf-8 -*-

"""
@author:yankerp
@url:www.yankerphub.com
"""

# from fuu import x # 指向foo内x对应的内存地址
# 当foo内的x的值发生变化，这里的x不会有任何的改变。这里的x还是以定义的阶段为准
# from fuu import get
# from fuu import change
#
# print(x)
# get()
# change()
# get()
#
# from fuu import x
# print(x)

import foo
foo.change()
foo.get()
print(foo.x)