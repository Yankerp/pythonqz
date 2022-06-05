# -*- coding utf-8 -*-

"""
@author:yankerp
@url:www.yankerphub.com
"""

# l = ['yanzan', 'zhangsan', 'lisi']
#
# count = 0
# while True:
#     # if count == l.__len__():
#         break
#     else:
#         print(l[count])
#         count += 1


# l1 = {
#     'name': 'yanzan',
#     'age': 19
# }
#
# count = 0
# while True:
#     if count == l1.__len__():
#         break
#     else:
#         print(l1[count])


# # 字符串
# "yanzan".__iter__()  # 存在iter证明字符串是可迭代对象
#
# # 列表
# ['111','222','3333'].__iter__() # 存在iter证明列表是可迭代对象
#
# # 字典
# {'name' : 'yanzan'}.__iter__() # 存在iter证明字典是可迭代对象
#
# # 元组
# (1,2,3,4).__iter__() # 存在iter 证明元组是可迭代对象
#
# # 集合
# {1,2,3,4}.__iter__() # 存在iter 证明集合类型是可迭代对象
#
# # 文件
# with open('wolai.py', mode='rt', encoding='utf-8') as f:
#     f.__iter__()   # 文件存在iter，证明文件是可迭代对象
#
# # 整型
# nmber = 123
# nmber.__in  # 不存在iter
# # 浮点型
# nmber2 = 1.1
# nmber2.__i  # 不存在iter


# user_info = {'yanzan', 'zhangsan', 'lisi'}
# user_info_iter = user_info.__iter__()
# print(user_info_iter.__next__())
# print(user_info_iter.__next__())
# print(user_info_iter.__next__())
# print(user_info_iter.__next__())


# user_info = {'yanzan', 'zhangsan', 'lisi'}
# user_info_iter = user_info.__iter__()
#
# while True:
#     try:
#         print(user_info_iter.__next__())
#     except StopIteration:
#         break  # 第一次取值走到这步的时候，证明userinfo里面的值已经取干净了，这个时候的指针就是在末尾
#
#
# print("这是第二次取值咯".center(50, '*'))
# while True:
#     try:
#         print(user_info_iter.__next__())
#     except StopIteration:
#         break


# with open('笔记', mode='rt', encoding='utf-8') as f:
#     while True:
#         try:
#             print(f.__next__())
#         except StopIteration:
#             break


# user_info = {'yanzan', 'zhangsan', 'lisi'}
# user_info_iter = user_info.__iter__() # 调用可迭代对象iter方法得到一个迭代器对象。
#
# user_info_iter.__iter__() # 迭代器对象存在iter方法
# user_info_iter.__next__() # 迭代器对象同时也存在next方法
#
# res = user_info_iter.__iter__()
# print(res is user_info_iter)


# # 列表
# ['111','222','3333'].__iter__() # 存在iter证明列表是可迭代对象
#
# # 字典
# {'name' : 'yanzan'}.__iter__() # 存在iter证明字典是可迭代对象
#
# # 元组
# (1,2,3,4).__iter__() # 存在iter 证明元组是可迭代对象
#
# # 集合
# {1,2,3,4}.__iter__() # 存在iter 证明集合类型是可迭代对象
#
# # 文件
# with open('wolai.py', mode='rt', encoding='utf-8') as f:
#     f.__iter__()   # 文件存在iter，证明文件是可迭代对象
#     f.__next__()   # 文件同时存在iter和next，说明文件类型是迭代器对象


#
# user_info = {'yanzan', 'zhangsan', 'lisi'}
#
# res = user_info.__iter__()
# while True:
#     try:
#         print(res.__next__())
#     except StopIteration:
#         break
#
# for name in user_info:
#     print(name)


'''
1、for循环in后面必须是可迭代对象，调用user_info.__iter__方法得到一个迭代对象
2、得到的迭代器对象执行next方法得到的值赋值给变量name
3、重复第二步的操作一直next取值赋值给变量name，将取干净后for循环会自动处理抛出的StopIteration信息，结束for循环
'''

# print("hello world")
# yield
# print(1)
# yield
# print(2)
# yield
# print(3)
# yield
# print(4)
# yield
# print(5)
# yield
# print(6)
# yield
# print(7)
# yield
# aaa = func()  # 获得一个生成器的对象，生成器就是自定义的一个迭代器对象
# aaa.__next__()  # 这个生成器里面有next方法
# aaa.__next__()  # 这个生成器里面有next方法
# aaa.__next__()  # 这个生成器里面有next方法
# aaa.__next__()  # 这个生成器里面有next方法
# aaa.__next__()  # 这个生成器里面有next方法
# aaa.__next__()  # 这个生成器里面有next方法
# aaa.__next__()  # 这个生成器里面有next方法
# aaa.__next__()  # 这个生成器里面有next方法





def func():
    count = 0
    while True:
        print(count)
        count += 1
        yield

res = func()
while True:
    print(res.__next__())