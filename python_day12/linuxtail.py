# -*- coding utf-8 -*-

"""
@author:yankerp
@url:www.yankerphub.com
"""
# import time
# with open(r'/Users/ayao/PycharmProjects/pythonqz/python_day12/accesszz.log', mode='rb') as f:
#     f.seek(0,2)
#     while True:
#         res = f.readline()
#         if len(res) == 0:
#             time.sleep(1)
#         else:
#             print(res.decode('utf-8'))


# with open('accesszz.log', mode='rb') as f:
#     f.seek(-2, 2)
#     print(f.tell())
#     res = f.read()
#     print(res)  # \N也是一个字节哦
#     f.seek(0, 2)
#     print(f.tell())
#
# with open('accesszz.log', mode='ab') as f:
#     f.seek(0, 2)
#     f.write('延瓒真帅，这是末尾的字节指针'.encode('utf-8'))

with open('aaaa.txt', mode='rb') as f:
    f.read('10')
    f.seek(-10, 2)
    print("现在指针的位置是在{num}".format(num=f.tell()))
    res = f.read()
    print(res)
