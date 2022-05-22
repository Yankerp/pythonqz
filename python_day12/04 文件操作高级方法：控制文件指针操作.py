# -*- coding utf-8 -*-

"""
@author:yankerp
@url:www.yankerphub.com
"""

# 指针移动的单位都是以字节为单位的bytes
# 只有一种情况特殊：
#       t模式的read(n) 这个n代表的是字符的个数

# with open('aaaa.txt', mode='rt', encoding='utf-8') as f:
#     res = f.read(3)  # 读出3个字符
#     print(res)

# 控制指针的移动叫f.seek()：是以字节bytes为单位的
# f.seek(n,mode) n:指的是移动的字节个数
''' mode
模式：
    0：参照物是文件开头的位置
    1：参照物是当前指针所在的位置
    2：参照物是文件末尾的位置
f.tell() # 获取文件当前指针的位置，都是以字节为单位的
强调：只有0模式可以在t下使用，1和2都不行，因为操作指针来讲都是根据bytes字节的类型
'''

# 示范
# with open('aaaa.txt', mode='rb') as f:
#     f.seek(9, 0)
#     f.seek(3, 0)
#     print(f.tell())
#     res = f.read()
#     print(res.decode())


# linux tail -f命令实现
import time
with open('aaaa.txt', mode='rt', encoding='utf-8') as f:
    f.seek(0, 2)
    while True:
        res = f.readline()
        if len(res) == 0:
            time.sleep(1)
        else:
            print(res)








