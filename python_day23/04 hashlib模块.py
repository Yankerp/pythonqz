# -*- coding utf-8 -*-

"""
@author:yankerp
@url:www.yankerphub.com
"""

# 1、什么是哈希hash
#   hash一类算法，该算法接收传入的内容，经过运算得到一串hash的值
#   hash值的特点：
#               1、只要传入的内容一样，得到的hash值必然一样
#               2、不能由hash值反解成内容
#               3、只要使用的hash算法不变，无论校验内容有多大，得到hash值长度是固定不变的


# 2、hash的用途

# pwd123------MD5----------->hash字符串
# 客户端--------hash字符串---------->服务端
#                                   hash字符串


# 3、如何用hashlib模块
# import hashlib
#
# m = hashlib.md5() # 括号内必须是bytes类型
# m.update('hello'.encode('utf-8'))
# m.update('world'.encode('utf-8'))
# res = m.hexdigest() #"helloworld"
# print(res)


# 模拟撞库
pass


# 提升撞库的成本--->密码加盐
import hashlib
m = hashlib.md5()
m.update("天王".encode('utf-8'))
m.update("alex3714".encode('utf-8'))
m.update("盖地虎".encode('utf-8'))
print(m.hexdigest())