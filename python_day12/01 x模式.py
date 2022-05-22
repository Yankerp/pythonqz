# -*- coding utf-8 -*-

"""
@author:yankerp
@url:www.yankerphub.com
"""

"""
x的模式默认只能写，不能读，如果文件存在则报错，如果文件不存在可直接创建
"""

with open('a.txt', mode='xt', encoding='utf-8') as f:
    f.write('this is a yankerp')  # 当a.txt文件存在时直接报错，不存在的时候则创建文件。
"""
Traceback (most recent call last):
  File "/Users/ayao/PycharmProjects/pythonqz/python_day12/01 x模式.py", line 12, in <module>
    with open('a.txt', mode='xt', encoding='utf-8') as f:
FileExistsError: [Errno 17] File exists: 'a.txt'
"""



