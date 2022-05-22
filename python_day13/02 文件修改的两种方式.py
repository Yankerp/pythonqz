# -*- coding utf-8 -*-

"""
@author:yankerp
@url:www.yankerphub.com
"""

# 文件修改的两种方式


"""第一种方式"""  # 这个是有问题的，直接通过read读
# with open('file.txt', mode='rt', encoding='utf-8') as f:
#     res = f.read()
#     name = res.replace('延瓒', '张三')
#
# with open('file.txt', mode='wt', encoding='utf-8') as f2:
#     f2.write(name)

"""第二种方式"""
import os

with open('file.txt', mode='rt', encoding='utf-8') as f, \
        open('file2.txt', mode='wt', encoding='utf-8') as f2:
    for line in f:
        f2.write(line.replace('张三', '延瓒'))

os.replace('file2.txt', 'file.txt')  # 在这里用的是replace，替换的方式，类似于剪切，课程中用的方式是rename修改文件名的方式

# 计算机的每一个文件在硬盘当中都没有修改的概念，都是将数据读到内存进行内存修改最终在写到数据库的一个操作，在硬盘当中只有覆盖的说法，没有修改的一回事
