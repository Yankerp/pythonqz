# -*- coding utf-8 -*-

"""
@author:yankerp
@url:www.yankerphub.com
"""


# 函数对象
# def func():  #  在这里的func等于 func = 函数体的内存地址
#     print('hello world')
#
# func()

# 1、可以将func的内存地址赋值给其他的变量名来用
# 例如
# def func():
#     print('hello world')
#
# res = func
# print(res, func)


#
# def func():
#     print('hello world')
#
# def fooo(x):
#     print(x)
#
# fooo(func)

#
# def func():
#     return 'ok'
#
# def fooo(x):
#     return x
#
# res = fooo(func())
# print(res)
#
# #

#
# def func():
#     print('hello world')
#
#
# l = [111,2223,333,444,555,func]
# print(l)

#
# def func():
#     print('hello world')
#
# dict_s = {
#     'name' : 'yankerp',
#     'age' : 19,
#     'world' : func
# }
#
# print(dict_s)


# def func():
#     print('hello world')
#
#
# l = [111,2223,333,444,555,func]
# res = l[5]
# res()


# def func():
#     print('hello world')
#
# dict_s = {
#     'name' : 'yankerp',
#     'age' : 19,
#     'world' : func
# # }
# #
# # dict_s['world']()
#
#
#
# def Login():
#     print('登录')
#
# def register():
#     print('注册')
#
# def Withdrawal():
#     print('取款')
#
# def deposit():
#     print('存款')
#
# def Transfer():
#     print('转账')
#
# def quit():
#     print('退出程序')
#
#
# while True:
#     print("""
#     1 登录
#     2 注册
#     3 取款
#     4 存款
#     5 转账
#     q 退出程序
#     """)
#     your_xuanxiang = input('请你输入选项：').strip()
#     if your_xuanxiang == 'q':
#         break
#     if your_xuanxiang == '1':
#         Login()
#     elif your_xuanxiang == '2':
#         register()
#     elif your_xuanxiang == '3':
#         Withdrawal()
#     elif your_xuanxiang == '4':
#         deposit()
#     elif your_xuanxiang == '5':
#         Transfer()
#     else:
#         print("您输入的选项有误")

#
# def Login():
#     print('登录')
#
#
# def register():
#     print('注册')
#
#
# def Withdrawal():
#     print('取款')
#
#
# def deposit():
#     print('存款')
#
#
# def Transfer():
#     print('转账')
#
#
# def quit():
#     print('退出程序')
#
#
# xuan = {
#     '1': ['1 登录', Login],
#     '2': ['2 注册', register],
#     '3': ['3 取款', Withdrawal],
#     '4': ['4 存款', deposit],
#     '5': ['5 转账', Transfer],
#     'q': ['q 退出程序', None]
# }
#
# while True:
#     for x in xuan:
#         print(xuan[x][0])
#     your_xuanze = input("请您输入选项：").strip()
#     if your_xuanze == 'q':
#         quit()
#
#     if not your_xuanze.isdigit():
#         print('必须输入的是数字不能是其他字符')
#
#     if your_xuanze in xuan:
#         xuan[your_xuanze][1]()
#     else:
#         print('您输入的数字不存在请重新输入')




# def func():
#     print('ths is a func')
#
# def foo():
#     func()
#
# f


# def func1():
#     def func2():
#         print('hello world')
#     func2()

#
# func1()




# 闭包函数？

# 闭函数
# def func1():
#     def func2():
#         print('hello world')


# 包函数
# def func1():
#     x = 333333333
#     def func2():
#         print(x)


# def func1():
#     x = 3333333333
#     def func2():
#         print(x)
#     return func2
#
# res = func1()
# x = 44444444444444444
# res()  # 函数func2






# def func(x):
#     print(x)
#
# func(111111)


# def fun(x):
#     def func():
#         print(x)
#     return func
#
# res = fun(333333333)
# res()



# 方式1：
# import requests
# def get(url):
#     res = requests.get(url)
#     print(len(res.text))
#
# get('https://www.baidu.com')
# get('https://www.csdn.net')
# get('https://zhuanlan.zhihu.com/p/401129069')


# 方式二：
import requests
def get_url(url):
    url = url
    def get():
        res = requests.get(url)
        print(len(res.text))
    return get

baidu = get_url('https://www.baidu.com')
baidu()

csdn = get_url('https://www.csdn.net')
csdn()

zhihu = get_url('https://zhuanlan.zhihu.com/p/401129069')
zhihu()


# 总结：直接传递参数简单，但是非要用什么闭包的形式传入参数，就觉得多此一举吧。
# 提交github成功啦！！！！








