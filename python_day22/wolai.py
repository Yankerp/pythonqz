# -*- coding utf-8 -*-

"""
@author:yankerp
@url:www.yankerphub.com
"""

import time
import datetime

# print(time.time())


# def ok():
#     start = time.time()
#     time.sleep(1)
#     print("helloworld")
#     stop = time.time()
#     result = stop - start
#
#     print("运行的时间为{time1}".format(time1=result))
#
# ok()

#
# print(time.strftime("%Y-%m-%d %H:%M:%S"))
# print(time.strftime("%Y-%m-%d %X"))


#
# y_time = time.localtime()
# print(y_time.tm_year)
# print(y_time.tm_mon)
# print(y_time.tm_mday)
# print(y_time.tm_hour)
# print(y_time.tm_min)
# print(y_time.tm_sec)

# print(datetime.datetime.now()) # 直接获取到当前时间不需要%Y%M这些东西了，一步到位格式化的时间
# print(datetime.datetime.now() + datetime.timedelta(days=3))  # 可以计算三天后的时间，这个功能很牛逼
# print(datetime.datetime.now() - datetime.timedelta(days=3))  # 当前时间减了3天
# print(datetime.datetime.now() + datetime.timedelta(days=-3))  # 三天前的时间
# print(datetime.datetime.now() + datetime.timedelta(weeks=1))  # 一周后的时间
# print(datetime.datetime.now() + datetime.timedelta(days=365*3))  # 三年后的时间......


# d1 = time.time() # 获取了时间戳
# d2 = time.localtime(d1)  # 将d1时间戳转换为结构化时间
# d3 = time.strftime("%Y-%m-%d %H:%M:%S", d2) # 将d2的结构化时间转换为字符串格式化时间
#
# print(d1)
# print(d2)
# print(d3)


# d1 = time.strftime("%Y-%m-%d %H:%M:%S")  # 获取了字符串的格式化时间
# d2 = time.strptime(d1, "%Y-%m-%d %H:%M:%S") # 将字符串格式化时间转换为结构化时间
# d3 = time.mktime(d2)
#
# print(d1)
# print(d2)
# print(d3)


import random

def verification(count: int) -> str:
    res = ''
    for i in range(count):
        s1 = chr(random.randint(65, 90))  # a-z的大写字符
        s2 = chr(random.randint(65, 90)).lower()  # a-z的小写字母
        s3 = str(random.randint(1, 9))  # 1-9内的随机数字
        res += random.choice([s1, s2, s3])  # 随意选取一个东西
    return res

res = verification(100)
print(res)











