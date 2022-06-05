# -*- coding utf-8 -*-

"""
@author:yankerp
@url:www.yankerphub.com
"""

'''
1、什么是迭代器
    迭代器指的就是迭代取值的工具
    迭代是什么意思？
        迭代是一个重复的过程，每次重复都是基于上一次的结果继续的，单纯的重复并不是迭代

2、为何要有迭代器
    迭代器就是循环取值得一个工具，而涉及到能够把多个值循环取值出来的类型有：
    列表、字符串、元组、字典、集合、文件
    
    l = ['yanzan','zhangsan','lisi']
    
    count = 0
    while count < len(l):
        print(l[count])
        count+=1
    
    以上的循环取值是针对于index索引的数据类型：列表、字符串、元组。
    为了解决索引循环迭代取值的局限性，python必须提供一种能够不依赖索引的取值方式。这个就是迭代器
    
    迭代器解决了循环迭代取值索引+非索引取值的一个功能
    
3、如何用迭代器


'''

# 可迭代对象：但凡内置方法里面存在__iter__方法的都是可迭代对象、可以迭代的对象
# name = 'yanzan'
# l = []
# dicto = {}
# jihe = {1,2,3}
# yuanzu = ()
#
# with open('wolai.py', mode='rt', encoding='utf-8') as f:
#     # f.__iter__()
#     pass
# name.__iter__()
# l.__iter__()
# dicto.__iter__()
# jihe.__iter__()
# yuanzu.__iter__()


# 没有索引的可迭代对象为例：
# 调用可迭代对象下面的.__iter__方法会得到一个迭代器对象，会将其转换成迭代器，可迭代对象可以理解为可以转换成迭代器的对象
d = {'name':'yanzan','age':19,'pwd':'pwd123.com'}
# diter = d.__iter__()
# print(diter)  # <dict_keyiterator object at 0x7f8e7ec96950>
#
# print(diter.__next__())
# print(diter.__next__())
# print(diter.__next__())
# print(diter.__next__())  # 取干净以后抛出异常:StopIteration，结束信号，表示取值取干净了，没有值可取了

# diter = d.__iter__()
# while True:
#     try:
#         print(diter.__next__())
#     except StopIteration:
#         break

# diter = d.__iter__()
# while True:
#     try:
#         print(diter.__next__())
#     except StopIteration:
#         break
#
# print("----------------------------")
# diter = d.__iter__()
# while True:  # 在一个迭代器取值取干净的情况下，在对其取值就取不到，没值了
#     try:
#         print(diter.__next__())
#     except StopIteration:
#         break

l = [1,2,3,4,5,6,7,8,]

# liter = l.__iter__()
# while True:
#     try:
#         print(liter.__next__())
#     except StopIteration:
#         break

'''
with open('wolai.py', mode='rt', encoding='utf-8') as f:
    fiter = f.__iter__()
    while True:
        try:
            print(fiter.__next__())
        except StopIteration:
            break

with open('wolai.py', mode='rt', encoding='utf-8') as f:
    for x in f:
        print(x)
'''

# 3、什么是可迭代对象与迭代器对象详解
# 可迭代对象可以理解为可以转换成迭代器的对象： 内置有__iter__方法的对象
#   调用可迭代对象的__iter__方法会得到一个迭代对象
# 迭代器对象：内置有__next__方法的并且内置有__iter__方法的对象
#   调用迭代器对象__next__方法会得到迭代器的下一个值
#   调用迭代器对象__iter__方法会得到一个迭代器本身，说白了，调了和没调是一样的


user_info = {'name' : 'yanzan'}
user_info_iter = user_info.__iter__()


# print(user_info_iter.__iter__() is user_info_iter)
# user_info_iter.__next__()


# 可迭代对象：字符串、列表、字典、元组、集合、文件对象
# 迭代器对象：文件对象
# name = 'yanzan'
# l = []
# dicto = {}
# jihe = {1,2,3}
# yuanzu = ()
#
# name.__iter__()
# l.__iter__()
# dicto.__iter__()
# jihe.__iter__()
# yuanzu.__iter__()
#
# with open('wolai.py', mode='rt', encoding='utf-8') as f:
#     f.__iter__()
#     f.__next__()


# for循环的工作原理：for循环可以称之为迭代器/迭代循环
# d = {'name':'yanzan','age':19,'pwd':'pwd123.com'}

# 1、调用后面对象的.__iter__方法得到一个迭代器对象
# 2、调用得到的迭代器对象下面的__next__方法拿到一个返回值并且赋值给k
# 3、循环往复步骤二的操作，直到抛出异常stopiteration，for循环帮我们捕捉一样并且结束循环。
# for k in d:
#     print(k)

# with open('wolai.py', mode='rt', encoding='utf-8') as f:
#     for x in f:
#         print(x)


# 迭代器优缺点总结：
"""

"""













