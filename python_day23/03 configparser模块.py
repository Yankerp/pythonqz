# -*- coding: utf-8 -*-

"""
@author:yankerp
@url:www.yankerphub.com
"""

# 加载某种特定格式的配置文件
import configparser
config = configparser.ConfigParser()
config.read('test.ini')

# 1 获取sections
# print(config.sections())


# 2 获取某一个sections下的所有配置项：options
# print(config.options('section1'))


# 3、获取items
# print(config.items('section1'))


# 4、h
print(config.get('section1', 'name'))
print(config.get('section2', 'k1'))

print(config.get('section2', 'age')) # 读出来的数字是字符串
print(config.getint('section2', 'age')) # 读出来的数字是字符串，自动转成int类型

print(config.getboolean('section2', 'ok')) # get 布尔值
print(config.getfloat('section2','xinzi')) # 直接转成float浮点型








