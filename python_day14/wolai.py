# python函数的形参与实参

# 1、形参与实参的介绍：
# 形参
# def func(name, password): # 在函数定义的时候所定义的参数叫做形参
#     print(name, password)
# func('yanzan', 'pwd123.com')

# 位置参数：
# def func(x, y, z):
#     print(x, y, z)
#
# func(1, 2)

# 关键字参数：
# def func(x, y, z):
#     print(x, y, z)
#
# func()


# **补充：关键字实参与位置实参的一个结合应用：**

# def func(x, y, z):
#     print(x, y, z)
#
#
# func(z='zhangsan', 1, 2,)

# 默认参数：
# def func(name, age, url="中国"):
#     print("你的名字是{name}, 你的年龄是{age},你的地区是：{url}".format(name=name, age=age, url=url))
#
#
# func("延瓒", 20)
# func('张三', 22, url='美国')

#
# def func(x, y = 1 + 1):  # y的值是在定义函数的时候就被赋值，而不是调用的时候
#     print(x, y)
#
# func(1)


# 不建议使用
# def func(x, y, z=[]):
#     print(x, y, z)
#
# func(1, 2, z=['aaa', 111, 222])
#
#
# def func2(x, y, z=None):
#     if z is None:
#         z = []
#     z.append(x)
#     z.append(y)
#     print(x, y, z)
#
# func2(1, 2)


# 到此做一个小的总结：
"""
在以上学习的函数中总结如下：
1、一个函数分为两个部分，定义函数和调用函数
2、在定义函数的时候不会对函数体内的代码运行，但是会检查函数体代码的一些语法是否正确
3、定义函数的参数这个方面分为两个：一个是形参一个是实参
4、形参就是在定义函数的时候定义的参数，这个参数可以理解为变量名
5、实参就是在调用函数额阶段传入的参数，这个参数可以理解为变量值
6、在参数部分形参有两种参数的定义方式分别是：默认参数和位置参数
7、在参数部分的实参有两种传入方式分别是位置传递参数和关键字传递参数
8、在默认参数和关键字参数对于调用来讲，关键字参数必须要在位置参数之后
9、在默认参数和位置参数对于定义来讲，默认参数必须要在位置参数之后
"""


# 可变长度参数
# def userinfo(a, b, c, d, e, f, g, h, i,):
#     print('hello world')
#
#
# userinfo(1, 2, 3, 4, 5, 6)

# def userinfo(a, b, *args):
#     print(a, b, args)
#
#
# userinfo(1, 2, 3, 3, 4, 5, 5, 5, 6, 6, 7, 6, 6, 6, 7, 8, 8, 9, 9, )

# def userinfo2(*zzz, **zzzz):
#     print(zzz, zzzz)
#
#
# userinfo2(1, 2, 3, 3, 4, 2, 1, 1, 2, 12, 1, 2, 12, 1, 2, 12, 12, 1, 2, 31, 3, 12, 31, 23, 12, 3, 123, 12, 3, 12, 3, 12,
#           3, 12, 3, 12, 31, 23, 12, 3, 12, 3, 12, 3, 123, 1, 3, 12, 3, 12, 31, 3, 1, name='yanzan',password=123123123123)


#
# def func(x, y, *args):
#     print(x, y, args)
#
# func(*['111','222', '333','444'])
# func(*"this a yankerp")


# def func(x, y, *args, name=None, password=None):
#     print(x, y, args, name, password)
#
#
# func(1, 2, 3, 4, name='yanza', password='pwd123.com', 'age'='123123')


# def func(x, y, *args, name=None, password=None, **kwargs):
#     print(x, y, args, name, password, kwargs)
#
#
# func(1, 2, 3, 4, name='yanza', password='pwd123.com', age='19', shengao=190)
#
# # >>  1 2 (3, 4) yanza pwd123.com {age : 19, shenggao : 190}


# def func(*args, **kwargs):
#     print(args, kwargs)
#
#
# func(**{'name': 'yanzan', 'password': 'pwd123.com', 'url': 'ywyankerp.com'})
#
#
# def func2(*args, name=None, password=None, url=None):
#     print(args, name, password, url)
#
#
# func2(**{'name': 'yanzan', 'password': 'pwd123.com', 'url': 'ywyankerp.com'})


# def func(x, y, z, *args, oooo=None, **kwargs):
#     print(x, y, z, args, oooo, kwargs)
#
#
# func('zhangsan', 'lisi', *[1, 2, 3, 4, 5, 6, 7, 8, 9], oooo='哈哈哈哈哈',
#      **{'name': 'yankerp', 'age': 19, 'url': 'www.baidu.com', 'shengao': 190})
#
# # 预言函数输出成功！
# # >> zhangsan lisi 1 (2 3 4 5 6 7 8 9) 哈哈哈哈哈 {'name': 'yankerp', 'age': 19, 'url': 'www.baidu.com', 'shengao': 190}


# def index(a, b, c, e, f):
#     print('index>>>', a, b, c, e, f)
#
#
# def warppper(a, b, c, d, f):
#     print('warpper>>>', a, b, c, d, f)
#     index(a, b, c, d, f)
#
#
# warppper(1, 2, 3, 4, 5)




def index(a, b):
    print('index>>>', a, b)


def warppper(*args, **kwargs):
    print('warpper>>>', args, kwargs)
    index(args, kwargs)

warppper(1,2,3,4,5,6,name='yanzan')