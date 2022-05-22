# -*- coding utf-8 -*-

"""
@author:yankerp
@url:www.yankerphub.com
"""

# 1、打开文件
# open('/Users/ayao/PycharmProjects/pythonqz/python_day11/本周内容笔记')
f = open('a.txt', mode='rt')  # res的值是一种变量，占用了应用程序的内存空间  r是只读，t是文本文件
print(type(f))  # <class '_io.TextIOWrapper'> 文件类型
# x = 10  # 归属于python解释器的内存空间

# 2、操作文件：读和写
res = f.read()
盘  # 应用程序对文件的读写请求都是向操作系统发起系统的调用，随后又操作系统发起硬盘控制把数据读入内存当中或者写入硬

# 3、关闭文件
f.close()  # 关闭操作系统打开的那个文件
# f.read() # 变量f还是存在的但是不能在读了，因为文件已经关闭了.

"""
为什么要回收操作系统打开的文件呢，是因为操作系统可打开的文件数是有限的，最大是65535 ，并不是无限的一个资源。 打开文件的数目会限制操作系统的资源。
但是每次操作完文件都需要close关闭，如果不close关闭的话操作系统也会自动关闭，但会要过一段时间才会关闭. 会损耗性能，为了防止每次close关闭witch语法就出现了
witch语法解决了文件打开操作后不用手动close的问题。
"""
