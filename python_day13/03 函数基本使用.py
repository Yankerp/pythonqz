# -*- coding utf-8 -*-

"""
@author:yankerp
@url:www.yankerphub.com
"""

"""
1、什么是函数？
    函数就相当于一款工具具备某种功能
    函数的使用必须遵守一个原则：
        先定义
        后调用

2、为何要用函数
    1、组织结构不清晰，可读性很差
    2、代码重复性过多，代码冗余
    3、可维护性很差，扩展性差
    
3、如何用函数？
    先定义
        三种定义方式
    后调用
        三种调用方式
    返回值：
        三种放回方式
"""

# 1、先定义
'''
def 函数名(参数1.餐数2.....):
    """文档描述"""
    pass 代码块
    pass 代码块
    return 返回值
'''

'''形式一：无参函数'''
# def func():  # 函数的命名风格和变量名的命名风格是一样的, 函数是一个工具，尽量写成动词，而不是名词。
#     print()
#     print("哈哈哈哈")
#     print("哈哈哈哈")
#     print("哈哈哈哈")
#     print("哈哈哈哈")


# func()

"""定义函数发生的事情"""""
# 1、将函数体的代码保存到内存当中，申请内存空间保存函数体代码。
# 2、将上述内存地址赋值绑定给函数名 func。 函数的定义和变量=变量值的定义是一样的。
# 3、定义函数不会执行函数体代码，但是会检测对函数体的语法，要保证语法是正确的。

"""调用函数发生的事情"""
# 1、通过函数名找到函数的内存地址
# 2、然后将函数名后面加括号，就是在触发函数体代码的运行

# 示范1
# x = 11
# def bar(): # bar = 函数的内存地址
#     print('from bar')
#
# def foo():
#     print('from foo')
#     print(x)
#     bar()
#
# foo()


# 示范2：
# x = 11
# def foo():
#     print('from foo')
#     print(x)
#     bar()
#
# def bar():  # bar = 函数的内存地址
#     print('from bar')
#
# foo()


'''形式二：有参函数'''
# def func(x, y):  # 1赋值给了x，2赋值给了y  有参函数的函数在调用的时候必须传递参数调用
#     print(x, y)
# # 函数的参数就是变量名，调用的时候输入的参数就是变量名，可以理解为赋值的一个操作，变量名=变量值得操作
# func(1, 2)


'''形式三：空函数指的就是函数体代码为pass'''


# def func(x, y):
#     pass


# 三种定义方式各用在何处？
# 1、无参函数的应用场景
# def out_user():
#     your_name = input("请您输入您的名称：").strip()
#     your_password = input("请您输入您的密码：").strip()
#     msg = '名字：{}, 密码：{}'.format(your_name, your_password)
#     print(msg)


# 2、有参函数的应用场景
# def add(x, y):  # 参数是原材料，return返回的值就是加工后的产品
#     # x = 10
#     # y = 11
#     res = x + y
#     return res  # 返回值，返回x+y的一个计算结果
#
#
# res = add(10, 20)
# print(res)

# 3、空函数的应用场景: 构思代码的时候会用到空函数
"""
def user():
    pass


def password():
    pass


def ls():
    pass


def cd():
    pass


def pwd():
    pass
"""


# 二、调用函数的三种形式
# 1、语句的形式:只去调用函数不做任何的操作
# func()

# 2、表达式形式：传入参数的的调用
# def add(x, y):
#     a = x + y
#     return a
# 赋值表达式
# res = add(1, 2)
# res2 = add(1, 2)*10
# print(res)
# print(res2)

# 3、函数调用可以当做参数
# res = add(add(10,3), 10)
# print(res)

# 三、函数的返回值
# return: 函数体代码一旦遇到return会立刻结束终止函数的运行！
# 1、返回none：函数体内没有return、或者return没有值或者return none.......
# def func():
#     return   # 直接退出函数并返回return的结果
# res  = func()
# print(res)


# 2、返回一个值
# def func():
#     return  123 # 直接退出函数并返回return的结果
#
# res = func()
# print(res)

# 3、返回多个值：用逗号分隔开多个值,会被returnfa返回成元组
# def func():
#     return 10, 'aaa', 'zzz'


# res = func()
# print(res)  # (10, 'aaa', 'zzz')

