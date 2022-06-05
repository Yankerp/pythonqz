# -*- coding utf-8 -*-

"""
@author:yankerp
@url:www.yankerphub.com
"""


# 如何得到自定义的迭代器：
# 在函数内一旦存在yield关键字，调用函数并不会执行函数体代码，会返回一个生成器对象，生成器就是自定义的迭代器
#
# def func():
#     print("第一次")
#     yield 1
#     print("第二次")
#     yield 2
#     print("第三次")
#     yield 3
#     print("第四次")
#     yield 4
#
# g = func()
# print(g)  # <generator object func at 0x7f88975982e0>
# # 生成器tm的就是迭代器
# # g.__next__() # 会触发函数体代码的运行，遇到yield停下来，将yield后的值会当做本次调用的结果
#
# res = g.__next__()
# print(res)



def func():
    count = 0
    while True:
        count += 1
        yield count

res = func()
print(next(res))



