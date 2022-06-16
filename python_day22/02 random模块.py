# -*- coding utf-8 -*-

"""
@author:yankerp
@url:www.yankerphub.com
"""

import random


# 大于0且小于1之间的小数
# print(random.random())
#
# 大于等于1且小于等于3之间的整数(就是1-3 随机)
# print(random.randint(1, 3))
#
# 大于等于1且小于3之间的整数（顾头不顾尾）
# print(random.randrange(1, 3))
#
# choice就是在一个列表中有多个元素，随机选择其中一个元素
# print(random.choice([1, 'yazan', 666, 'zhangsan', 'wangwu', [8888888888888888]]))
#
# 和choice一样在一个列表中有多个元素，但是sample是可以选择一次选中几个(列表中任意两个组合)
# print(random.sample([1, 'yazan', 666, 'zhangsan', 'wangwu', [8888888888888888]], 2))
#
# 大于1小于3的小数
# print(random.uniform(1, 3))
#
#
# 打乱item的顺序,相当于"洗牌"
# item = [1, 3, 5, 7, 9]
# random.shuffle(item)
# print(item)


# 思考：生成6位随机验证码 字母+数字

# 已经实现，六位验证码（数字+小写+大写）
def verification(count: int) -> str:
    res = ''
    for i in range(count):
        s1 = chr(random.randint(65, 90))
        s2 = chr(random.randint(65, 90)).lower()
        s3 = str(random.randint(1, 9))
        res += random.choice([s1, s2, s3])
    return res