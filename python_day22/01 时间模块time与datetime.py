# -*- coding utf-8 -*-

"""
@author:yankerp
@url:www.yankerphub.com
"""
import time

# 时间模块优先掌握的操作

# 一、time
# 时间分为三种格式
# 1、时间戳：1970年到现在经历过的秒数，这个叫时间戳
#   作用：用于时间间隔的计算
# print(time.time())  # 获取时间戳

# 2、格式化的字符串形式（按照某种格式显示的时间）
#   作用：用于展示时间的
"2022-06-07 10:56:12"
# print(time.strftime("%Y-%m-%d %H:%M:%S"))
# print(time.strftime("%Y-%m-%d %X"))

# %X = %H:%M:%S
# %Y年
# %m月
# %d天
# %H小时
# %M分钟
# %S秒

# 3、结构化的时间
#   作用：用于单独获取时间的某一部分
# res = time.localtime()
# print(res) # time.struct_time(tm_year=2022, tm_mon=6, tm_mday=7, tm_hour=10, tm_min=59, tm_sec=28, tm_wday=1, tm_yday=158, tm_isdst=0)
# print(res.tm_year)
# print(res.tm_yday)


# 二、datetime
# import datetime
#
# print(datetime.datetime.now())  # 直接获取到当前时间不需要%Y%M这些东西了，一步到位格式化的时间
# print(datetime.datetime.now() + datetime.timedelta(days=3))  # 可以计算三天后的时间，这个功能很牛逼
# print(datetime.datetime.now() - datetime.timedelta(days=3))  # 当前时间减了3天
# print(datetime.datetime.now() + datetime.timedelta(days=-3))  # 三天前的时间
# print(datetime.datetime.now() + datetime.timedelta(weeks=1))  # 一周后的时间
# print(datetime.datetime.now() + datetime.timedelta(days=365*3))  # 三年后的时间......

import datetime


# 时间模块需要掌握的内容：
# 以下为：Timestamp时间戳转换为--->struct_time结构化时间--->format_string格式化字符串时间
# print(time.time())
# jiegouhua_time = time.localtime(1654582238.314019)
# print(jiegouhua_time)
#
# format_string = time.strftime("%Y-%m-%d %H:%M:%S", jiegouhua_time)
# print(format_string)

# 以下为：format_string格式化字符串时间--->struct_time结构化时间--->Timestamp时间戳
format_string = time.strftime("%Y-%m-%d %H:%M:%S")
print(format_string)
# format_string格式化字符串时间--->struct_time结构化时间
jiegouhua_time = time.strptime(format_string, "%Y-%m-%d %H:%M:%S")
print(jiegouhua_time)

# struct_time结构化时间--->Timestamp时间戳
print(time.mktime(jiegouhua_time))