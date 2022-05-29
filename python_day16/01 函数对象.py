# -*- coding utf-8 -*-

"""
@author:yankerp
@url:www.yankerphub.com
"""


# 函数对象的精髓：就是可以把函数当做变量去用
# func = 内存地址

# def func():
#     print('hello world')

# 1、可以将func对应的内存地址赋值给其他的变量呗
# res = func
# print(res, func)
# res()


# 2、可以当做函数的参数传入
# def func():
#     print('hello world')
#     return 'ok'

# def foo(x):
#     print(x)
#     x()
# foo(func)

# 3、可以当做函数当做另外一个函数的返回值
# def func():
#     print('hello world')
#     return 'ok'
#
# def foo(x):
#     return x
#
# res = foo(func)
# print(res)


# 4、














# ATM案例：

def login():
    print('登录功能')

def register():
    print('注册功能')

def withdrawal():
    print('取款功能')

def deposit():
    print('存款功能')

def transfer():
    print('转账功能')

def quit():
    print('退出程序')

while True:
    print("""
    0 登录功能 
    1 注册功能
    2 取款功能
    3 存款功能
    4 转账功能
    q 退出程序
    """)
    user_dict = {
        '0' : login,
        '1' : register,
        '2' : withdrawal,
        '3' : deposit,
        '4' : transfer,
        'q' : quit
    }
    your_xuanxiang = input('请您输入选项：').strip()
    if your_xuanxiang in user_dict:
        user_dict[your_xuanxiang]()
    else:
        print('不存在这个选项，请您重新输入')




