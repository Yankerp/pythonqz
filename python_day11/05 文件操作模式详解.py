# -*- coding utf-8 -*-

"""
@author:yankerp
@url:www.yankerphub.com
"""
# 先以t模式为基础基本操作
# 1、r（默认的操作模式）：只读模式，不能写
# 当文件不存在的时候会直接报错，当文件存在时，文件指针跳到最开始的位置
# with open('d.txt', mode='rt', encoding='utf-8') as f:
#     print("第一次读".center(60, "*"))
#     res = f.read() # 把文件的内容从当前所在的位置一下读到结尾------------指针的问题
#     print(res)
#     # 此时文件没有关，指针到了末尾，这个时候接下来在读得话就读不出来了
#     print("第二次读".center(60, "*"))
#     res1 = f.read()
#     print(res1)
#     # read当文件过大的时候这就出现了从当前位置直接读在内存，直接内存干爆，这是有局限性的。读出了所有的内容，所有的内容从硬盘读入硬盘

"""案例的优化"""
# username = 'yanzan'
# userpassword = 'pwd123'

# input_name = input("user:").strip()
# input_password = input('pass:').strip()
#
#
# if input_name == username and input_password == userpassword:
#     print("成功")
# else:
#     print("错误")

# 优化一：通过文件保存账号密码：
# with open('user.txt', mode='rt', encoding='utf-8') as f:
#     res = f.read()
#     uname, upwd = res.split(":")  # 单独的用户一行数据是不存在换行的问题
#
#     input_name = input("user:").strip()
#     input_password = input('pass:').strip()
#
#     if input_name == uname and input_password == upwd:
#         print("成功")
#     else:
#         print("错误")


# 优化二：
# input_name = input("user:").strip()
# input_password = input('pass:').strip()
#
# with open('user.txt', mode='rt', encoding='utf-8') as f:
#     for x in f:
#         uname, upassword = x.strip("\n").split(":")
#         if input_name == uname and input_password == upassword:
#             print("账号密码成功")
#             break
#     else:
#         print("账号密码没有找到失败！！！")

# 2、w只写模式：只能写不能读，当文件不存在的时候会直接创建一个空文件，若存在的话w会清空文件，指针到了开始的位置。
# with open("yanzan.txt", mode='wt', encoding="utf-8") as f:
#     f.write('哈哈哈哈\n')  # pspspsps：w会直接先清空文件中的所有内容，指针会在开始的位置，切记不能把关键文件用write写入不然会直接清空，数据无法找回
#     f.write("哈哈哈哈哈哈哈哈2\n")
#     f.write("哈哈哈哈哈哈哈哈3\n")

# 强调：
# 1、以w模式打开文件没有关闭的情况下连续的写的话总是跟在旧的内容之后
# with open("yanzan.txt", mode='wt', encoding="utf-8") as f:
#     f.write('哈哈哈哈\n')  # pspspsps：w会直接先清空文件中的所有内容，指针会在开始的位置，切记不能把关键文件用write写入不然会直接清空，数据无法找回
#     f.write("哈哈哈哈哈哈哈哈2\n")
#     f.write("哈哈哈哈哈哈哈哈3\n")

# 2、如果重新以w模式打开文件,会清空之前的内容重新写入内容：
# with open("yanzan.txt", mode='wt', encoding="utf-8") as f:
#     f.write('哈哈哈哈\n')
#
# with open("yanzan.txt", mode='wt', encoding="utf-8") as f:
#     f.write('哈哈哈哈\n')
#
# with open("yanzan.txt", mode='wt', encoding="utf-8") as f:
#     f.write('哈哈哈哈张三\n')

"""写入
"""

# 3、a只追加写，当文件不存在的时候会直接创建文件，若文件存在则指针直接调到末尾。
with open("eee.txt", mode="at", encoding="utf-8") as f:
    # f.read() # 不能读
    f.write("yankerp ")  # 默认写在最后
    f.write("yankerp1 ")  # 默认写在最后
    f.write("yankerp2 ")  # 默认写在最后
    f.write("yankerp 3")  # 默认写在最后

# 强调：a与w模式的相同点与不同点
"""
相同点：在open打开文件不关闭的情况下后续再次写入文件都会追加到文件的末尾，连续写入，新的内容总是会跟在前面写的内容之后
不同点：不同点在与，a模式打开文件不会删除文件的内容指针会直接跳到末尾，而w模式会直接清空文件的内容指针会移动到最开始的位置

a模式永远指针都是在最后末尾的位置追加。   w的写都是一个全新的写，通常用w来写新的文件，a的写是一个旧文件追加新内容的文件，通常用来追加旧的文件。在旧文件的基础之上增加内容
"""

# 案例：a模式在原来文件的内容基础之上存入内容，比如日志，或者注册功能持续存储的场景
# ========================注册功能，将用户名密码存入后台文件当中a模式场景
# 注册功能
# name = input("username:")
# pwd = input("password:")
#
# with open("dbd.txt", mode="at", encoding="utf-8") as f:
#     f.write('{name}:{pwd}\n'.format(name=name, pwd=pwd))


# 案例：w 文件拷贝的工具实现
# ========================w模式,

yuan_file = input("请输入源文件：").strip()
mub_file = input("请输入目标文件：").strip()

with open(yuan_file, mode='rt', encoding='utf-8') as f, \
        open(mub_file, mode='wt', encoding='utf-8') as f2:
    res1 = f.read()
    f2.write(res1)
    print(f"写入文件成功，请查看{mub_file}".format(mub_file=mub_file))

# 可读可写（+模式）不能单独使用，必须配合，r、w、a「了解内容」 +的模式了解即可，有很大的局限性
