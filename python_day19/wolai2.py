# -*- coding utf-8 -*-

"""
@author:yankerp
@url:www.yankerphub.com
"""

# def func():
#     while True:
#         what = yield 'running~'
#         print("延瓒今天中午吃了{what}".format(what=what))
#
# res = func()
# res.__next__()
# aaa = res.send('苹果')
# print(aaa)
#
# bb = res.send(['面条','米饭'])
# print(bb)


# def func(x, y):
#     if x > y:
#         return x
#     else:
#         return y

# print(func(1, 10))


# def func2(x, y):
#     return  x if x > y else y
#
# print(func2(1, 100))

# l = ['yanzan', 'zhangsan', 'lisi', 'wangwu']
#
# new_list = [name for name in l]
# print(new_list)


#
# l = ['yanzan', 'zhangsan', 'lisi', 'wangwu']
#
# new_l = [name.upper() for name in l]
# print(new_l)


# l = ['yanzan', 'zhangsan', 'lisi', 'wangwu']
#
# new_list = [name + "_game" for name in l]
# print(new_list)


# new_list = [name for name in l if name != 'wangwu']
# print(new_list)

# l = ['yanzan', 'zhangsan', 'lisi', 'wangwu']
# new_dict = {name:None for name in l}
# print(new_dict)


# items = [('name','egon'), ('age',18), ('gender','male')]
# new_dict = {key[0]:key[1] for key in items if 'gender' not in key}
# print(new_dict)


# info_list = (
#     ('yanzan','yanzan1','yanzan2'),
#     ('zhangsan','zhangsan1','zhangsan2'),
#     ('lisi','lisi1','lisi2')
# )
#
# jihe = {key for key in info_list}
# print(jihe, type(jihe))


#
# l = ['yanzan', 'zhangsan', 'lisi', 'wangwu']
#
# new_tuple = (name for name in l)
# print(new_tuple.__next__())
# print(new_tuple.__next__())
# print(new_tuple.__next__())
# print(new_tuple.__next__())
# print(new_tuple.__next__())  # 值已经取完了，抛出了异常：StopIteration
#
# with open('本周内容', mode='rt', encoding='utf-8') as f:
#     # print('笔记当中一共有{num}'.format(num=sum(len(n) for n in f.read())))
#     res = (len(n) for n in f.read())
#     print(sum(res))




# def func():
#     print("hello world")
#     func()
#
#
# func()


l = [333333,[123, [1212121, [1231],[23],[444],[12312312223222],[111111],[2222,[33333,[444,[5555,[66666]]]]]]]]

def func(list_1):
    for i in list_1:
        if type(i) == list:
            func(i)
        else:
            print(i)

func(l)
