# -*- coding utf-8 -*-

"""
@author:yankerp
@url:www.yankerphub.com
"""

# 1、什么是序列化&反序列化
# 序列化指的就是把内存的数据类型转换成一种特定的格式的内容，
# 该格式的内容可以用于存储或者传输给其他平台使用
#
#
# 1.1 序列化
# 内存中的数据类型-------->序列化--------->特定的格式（json&pickle格式）
#
# 1.2 反序列化
# 内存中的数据类型-------->反序列化<--------- 特定的格式（json&pickle格式）
#
#
# 土办法：
# {'name' : 'yanzan'} --------》序列化str('{'name' : 'yanzan'}')----->文件
# {'name' : 'yanzan'} <--------反序列化eval('{'name' : 'yanzan'}')<------文件
#
#
# 2、为何要序列化
# 用途：将内存当中的数据类型序列化后得到的特定格式的内容
#   1、该格式的内容可以用于存储-->用于存档
#   2、或者传输给其他平台使用-->跨平台数据交互
#      python中的列表------------------------------->java的数组
#      列表<--------------->特定的格式<-------------->数组
#          多种语言并存，多种语言的一种共同的标准特定格式
#   强调：
#       针对用途1的特定格式：是一种专用的格式，pickle只有python可以识别
#       针对用途2的特定格式，应该是一种通用的，能够被所有语言识别的格式--->Json格式
#
#       Json的格式并不能支持python的所有数据类型，这是一种全部语言通用格式。


# 一、如何序列化与反序列化
import json

# # 1 序列化
# # res = json.dumps(True)  # 序列化
# # print(type(res), res)  # <class 'str'> true  大True变小"true"，
#
# json_res = json.dumps([1, 'aaa', True, False])
# # print(type(json_res), json_res)  # [1, "aaa", true, false]
#
#
# # 2 反序列化
# l = json.loads(json_res)  # loads就是反序列化
# print(l, type(l))


# 示范：
import json

# 1 序列化 得到字符串格式，全部都是字符串
# res = json.dumps(True)  # 序列化
# print(type(res), res)  # <class 'str'> true  大True变小"true"，

# json_res = json.dumps([1, 'aaa', True, False])
# # print(type(json_res), json_res)  # [1, "aaa", true, false]
#
# with open('test.json', mode='wt', encoding='utf-8') as f:
#     f.write(json_res)

# 2 反序列化
# l = json.loads(json_res)  # loads就是反序列化
# print(l, type(l))

# with open('test.json', mode='rt', encoding='utf-8') as f:
#     res = json.loads(f.read())
#     print(res, type(res))


# 将序列化的结果写入文件的简单方法：
# with open('test.json', mode='wt', encoding='utf-8') as f:
#     json.dump([1, 'aaa', True, False], f)

# 从文件读取json格式的字符串进行反序列化的简单方法：
# with open('test.json', mode='rt', encoding='utf-8') as f:
#     l = json.load(f)
#     print(l)


# json验证：json格式是兼容所有语言通用的数据类型，不能识别某一语言所独有的类型
# json.dumps({1, 2, 3, 4, 5, })  # 集合：TypeError: Object of type set is not JSON serializable

# json强调：一定要搞清楚json格式，不要与python混淆
# res = json.loads('[1, "aaa", true, false]')
# print(res[0])




# 二、pickle和json使用方法一模一样
import pickle
# res = pickle.dumps({1,2,3,4,5,6})
# print(res)
#
# s = pickle.loads(res)
# print(s)


