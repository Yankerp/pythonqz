# -*- coding utf-8 -*-

"""
@author:yankerp
@url:www.yankerphub.com
"""

"""
        控制文件读写内容的模式：t和b
            强调：t和b不能单独使用，必须和r、w或者a连用
            t文本（默认的模式）
                1、默认读写都是以str（unicode）为单位的
                2、默认只针对文本文件
                3、必须指定encoding="utf-8" 编码成utf-8写入硬盘
"""

with open('c.txt', mode='rt',encoding='utf-8') as f:
    res = f.read()  # t模式会将f.read读出来的结果从utf-8解码成unicode，目前没有告诉open用什么格式读取，它用默认的格式用来读取，open打开的是操作系统的文件，所以
    # open打开的默认格式是通过操作系统默认的编码打开的文件。linux、unix、mac是utf-8，windows是用的GBK格式的编码。
    print(res)

with open('c.txt', mode='wt') as f:
    print(res)
    res = f.write('哈哈哈哈哈哈')  # 通过utf-8进行编码到硬盘

# 硬盘（c.txt文件目前在硬盘上的内容是utf-8格式的二进制）
# 内存：utf-8——————>解码----->unicode（str）
