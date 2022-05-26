# -*- coding utf-8 -*-

"""
@author:yankerp
@url:www.yankerphub.com
"""

# 函数的定义
'''
def 函数名(参数1，参数2):
    """描述信息"""
    代码1
    代码2
    代码3
    retrun 返回值
'''

# 无参函数
# 无参函数指的就是定义函数的时候没有传递或者定义任何的参数，直接就是函数名+()的形式的参数，简称为叫无参函数：
# def func():  # 函数的命名风格和变量名的命名风格是一样的, 函数是一个工具，尽量写成动词，而不是名词。
#     print("11111111111111111")
#     print("2222222222222222")
#     print("3333333333333333")
"""
- 将函数体的代码保存到内存当中，申请内存空间地址保存函数体代码
- 将上述函数体代码的内存地址赋值给变量名，也就是说赋值给函数名称
- 定义函数的时候不会执行任何的代码，但是会检测函数体内的语法格式，要保证语法格式是正确的。

1、通过函数的名字找到函数体的内存地址

2、然后将函数名后面加括号，就是在触发函数体代码的一个运行
"""

# def func():
#     print("this is a func1 ")
#
#
# def func2():
#     print('this is a func2')
#     func()
#
#
# func2()


# 有参函数的定义
"""
def func(x, y):  # 相当于定义了两个变量名叫做x、y。 那么这两个变量名是专门用来接收变量值。
    '''相当于，把这个1赋值给了变量x，把2赋值给了变量y'''
    print(x, y)  # 在这里调用变量名，打印出1，2


func(1, 2)
"""


# 空函数：
# def func():
#     pass
#
# def xxx():
#     pass

# 二、三种函数定义方式的应用场景
# 2.1、无参函数的应用场景
# def func():
#     your_name = input("yourname：").strip()
#     your_url = input("your_url：").strip()
#
#     res = "你的名字是{name}, 您的居住地址是：{url}".format(name=your_name, url=your_url)
#     print(res)
# func()

# 2.2、有参函数的应用场景
# def func(x, y):
#     res = x + y
#     res2 = x * y
#     res3 = x ** y
#     res4 = x - y
#     print(res, res2, res3, res4)
#     return res, res2, res3, res4
#
#
# res = func(1, 3)
# print(res)


# def func():
#     print("hello world")
#
# func()

#
# def fun(name, age):
#     return name, age
#
# result = fun('延瓒', 19)
# print(result)
#
# def func(name, age):
#     return name, age
#
# def func2(name1, age1):
#     return name1, age1
#
# res = func2(func('yanzan', 20), 19)
# print(res)


#
# def jisuan(x, y):
#     res = x + y
#     return res
#
# res = jisuan(jisuan(1, 1), 3)
# print(res)


# 三、返回值的三种方式
# 1、当函数体没有return或者return没有值或者return None的时候会返回空
# def func(x, y):
#     return
#
# name = func(1, 2)
# print(name)

# def func(x, y):
#     return None
# res = func(1, 2)
# print(res)

# def func(x, y):
#     res = x + y
#
# res = func(1, 2)
# print(res)

# 2、return返回一个值
# def func(x, y):
#     res = x + y
#     return  res
# res = func(1, 2)
# print(res)

# def func():
#     return 'hello world'
#
# res = func()
# print(res)

def user(name, url, age):
    return name, url, age

res = user('yanzan', 'www.yanzan.com', 19)
print(res)









