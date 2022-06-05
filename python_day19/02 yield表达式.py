# -*- coding utf-8 -*-

"""
@author:yankerp
@url:www.yankerphub.com
"""

# def dog(name):
#     print("{name}准备吃东西啦".format(name=name))
#     while True:
#         aaa = yield
#         print(type(aaa), aaa)
#         print("延瓒吃了一个{aaa}".format(aaa=aaa[0]))
#
#
# res = dog('延瓒')  # <generator object dog at 0x7fba55d9d2e0>获得了一个生成器，自定义的迭代器
# # res.send('苹果')   # TypeError: can't send non-None value to a just-started generator
#
# res.__next__()
# res.send('苹果')
# res.send('香蕉')
# res.send('葡萄')
# res.send('感知')
# res.send('零食')
# res.send(['牛逼','水'])


def dog(name):
    for_list=[]
    print("{name}准备吃东西啦".format(name=name))
    while True:
        aaa = yield for_list
        print("延瓒吃了一个{aaa}".format(aaa=aaa))
        for_list.append(aaa)


res = dog('延瓒')  # <generator object dog at 0x7fba55d9d2e0>获得了一个生成器，自定义的迭代器
# res.send('苹果')   # TypeError: can't send non-None value to a just-started generator

res.__next__()
result1 = res.send('苹果')
print(result1)
result2 = res.send('香蕉')
print(result2)
# res.send('葡萄')
# res.send('感知')
# res.send('零食')
# res.send(['牛逼','水'])