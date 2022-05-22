# -*- coding utf-8 -*-

"""
@author:yankerp
@url:www.yankerphub.com
"""

# with open('wolaidb.txt', mode='r+b') as f:
#     f.seek(6, 0)
#     num = f.tell()
#     print("现在的wolaidb文件内容的指针是在{n}".format(n=num))
#     f.write('指针的修改'.encode('utf-8'))

# import os
# with open('wolai.txt', mode='rb') as f:
#     for line in f:
#         res = line.decode('utf-8')
#         result = res.replace('延瓒', '张三')
#
# with open('wolai2.txt', mode='wb') as f2:
#     f2.write(result.encode('utf-8'))
#
# os.replace('wolai2.txt', 'wolai.txt')
"""
@author:yankerp
@url:www.yankerphub.com
"""

# with open('wolaidb.txt', mode='r+b') as f:
#     f.seek(6, 0)
#     num = f.tell()
#     print("现在的wolaidb文件内容的指针是在{n}".format(n=num))
#     f.write('指针的修改'.encode('utf-8'))
#
# import os
# with open('wolai.txt', mode='rb') as f:
#     res = f.read()
#     result = res.decode('utf-8')
#     result_txt = result.replace('张三ok', 'zhangsna')
#
# with open('wolai2.txt', mode='wb') as f2:
#     f2.write(result_txt.encode('utf-8'))
#
# os.replace('wolai2.txt', 'wolai.txt')
#


# import os
#
# with open('wolai.txt', mode='rb') as f, \
#     open('wolai2.txt', mode='wb') as f2:
#     for line in f:
#         result = line.decode('utf-8')  # result 这是一个字符串str
#         res = result.replace('我是zhangsna', '延瓒ok')
#         f2.write(res.encode('utf-8'))
#     os.replace('wolai2.txt', 'wolai.txt')

#
# with open('wolai.txt', mode='rb') as f:
#     while True:
#         res = f.read(1024)
#         if len(res) == 0:
#             break
#         else:
#             print(res)

# with open('smcs5.16.xlsx', mode='rb') as f2, \
#         open('smcs5.16_back.xlsx', mode='ab') as f3:
#     while True:
#         res = f2.read(100)
#         if len(res) == 0:
#             break
#         f3.write(res)
#         num = len(res)
#         aaa = f2.tell()
#         print(f"当前文件内容的指针在{aaa}")
#         print(res)
#         print("现在正在每行写入到最新的文件的bytes字节为：{num}".format(num=num))
