# -*- coding utf-8 -*-

"""
@author:yankerp
@url:www.yankerphub.com
"""


# 形参定义* **
# def func(name, *args, **kwargs):
#     print(name, args, kwargs)
#
#
# func('yanzan', 'zhangsan', 'list', password='pwd123.com')


# # 实参定义* **
# def func(name, *args, **kwargs):
#     print(name, args, kwargs)
#
# func(*['yanzan', 'wangwu', 'lisi'], **{'password' : 'pwd123.com', 'age' : 19})


# def func(a, b, c='yanzan', *args, **kwargs):
#     print(a, b, c, args, kwargs)
#
# func(1,2,3,4,5,6,7,8,9,0)


# def func(a, b, *args, c='yanzan', **kwargs):
#     print(a, b, c, args, kwargs)
#
# func(1,2,3,4,5,6,7,8,9,0)
# # 1 2 'yanzan' (3,4,5,6,7,8,9,0) {}


# def func(a, b, c, *args, name='yanzan', password='pwd123.com', **kwargs):
#     print(a, b, c, args, name, password, kwargs)
#
#
# func(1, 2, 3, 4, 5, age=19)

#
# def func(*z):
#     print(z)
#
# func(1,2,3,)


# def func(a, b, c=999, *args, **kwargs):
#     print(a, b, c, args, kwargs)
#
# func(1,2,3,4,5,6,7,8)


# with open('aaaa', mode='rb') as f:
#     res = f.read()
#     print(res)


# def file(filename):
#     '''读取某个文件内容的功能'''
#     with open(filename, mode='rt', encoding='utf-8') as f:
#         res = f.read()
#         print(res)
#
#
# file('aaaaa')  # 这是我的调用方式

# def outter(func):
#     def zhuce(*args, **kwargs):
#         your_name = input("name >>>> ")
#         your_password = input("password>>>")
#         if your_name == 'yanzan' and your_password == 'pwd123.com':
#             func(*args, **kwargs)  # 这是我的调用方式
#         else:
#             print("user or password error!!!!")
#
#     return zhuce
#
#
# @outter  # out = outter(out)
# def out(name, age):
#     print(name, age)
#
# out('yanzan', 19)

#
#
# def file(filename):
#     '''读取某个文件内容的功能'''
#     with open(filename, mode='rt', encoding='utf-8') as f:
#         res = f.read()
#         print(res)
#
#
#
# def zhuce(*args, func=None, **kwargs):
#     your_name = input("name >>>> ")
#     your_password = input("password>>>")
#     if your_name == 'yanzan' and your_password == 'pwd123.com':
#         func(*args, **kwargs)  # 这是我的调用方式
#     else:
#         print("user or password error!!!!")
#
#     return zhuce
#
# res = zhuce
# res('aaaaa', func=file)


def outter(func):
    def wapper(*args, **kwargs):
        func(*args, **kwargs)  # 这是我的调用方式

    return wapper


@outter  # out = outter(out)
def out(name, age):
    print(name, age)


@outter
def file(filename):
    '''读取某个文件内容的功能'''
    with open(filename, mode='rt', encoding='utf-8') as f:
        res = f.read()
        print(res)


out('yanzan', 19)
file('aaaaa')

# @outter
# def func(name=None):
#     print(name)
#
# func(name='11111111111111')


def func(name=None, **kwargs):
    print(name, kwargs)

func(**{'name' : 'yankerp','age':10})
