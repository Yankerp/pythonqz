# -*- coding utf-8 -*-

"""
@author:yankerp
@url:www.yankerphub.com
"""

salaries = {
    'yanzan': 3000,
    'tom': 7000,
    'lili': 10000,
    'jack': 2000
}
# 需求1：找出薪资最高的人
# res = max(salaries)
# print(res)

# 迭代出来的内容   比较的值
#    'yanzan'
#    'tom'
#    'lili'
#    'jack'

# def func(k):
#     return salaries[k]
#
# res = max(salaries,key=lambda k:salaries[k])  # 求最大的
# print(res)
#
#
# res = min(salaries,key=lambda k:salaries[k])  # 求最小的
# print(res)


salaries = {
    'yanzan': 3000,
    'tom': 7000,
    'lili': 10000,
    'jack': 2000
}

# sorted排序
res = sorted(salaries, key=lambda k: salaries[k], reverse=True)  # 默认加true就反过来排序从小到大，然后搞成列表
print(res)

# map(了解)
l = ['lxx', 'wxx', 'alex', 'xxq']
# new_list = [name + "_hahah"for name in l]
# print(new_list)
# 不学了，这些都是不常用的东西


# filter（了解）   不学了，直接听完了，这个没啥用

# reduce 这些都不常用...... 不学了
