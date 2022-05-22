# -*- coding utf-8 -*-

"""
@author:yankerp
@url:www.yankerphub.com
"""
# 一、读相关补充
# readline一次读一行
# with open('a.txt', mode='rt', encoding='utf-8') as f:
#     res1 = f.readline()
#     res2 = f.readline()
#     res3 = f.readline()
#     res4 = f.readline()
#     res5 = f.readline()
#     res6 = f.readline()
#     print(res1)
#     print(res2)
#     print(res3)
#     print(res4)
#     print(res5)
#     print(res6)


# readline全部读出来，存入列表当中
# with open('a.txt', mode='rt', encoding='utf-8') as f:
#     res = f.readlines()
#     print(res)

"""二、写相关的操作："""
# 1、writelines
# f.writelines就相当于for循环把列表当中的元素循环一个个写入到文件中因为write只能写入字符串
# l = ['111111','2222222','3333333']
# with open('a.txt',mode='wt',encoding='utf-8') as f:
#     f.writelines(l)

# 2、flush
with open('aaaa.txt', mode='at', encoding='utf-8') as f:
    f.write('哈哈哈哈')
    # f.flush()  # 立马写到硬盘当中去，大多数情况不用这个flush，对系统的性能存在影响
