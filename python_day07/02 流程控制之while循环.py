# 1、while循环的基本使用
'''
while 条件:
    代码1
    代码2
    代码3
'''

# count = 0
# while count < 5:
#     print(count)
#     count += 1


# 2、死循环的效率问题
# while True:  # io输出操作
#     print("hello world")
#
# while True:  # 终极死循环效率问题
#     100+100
# 纯计算的死循环会导致致命的效率问题

# 3、循环的应用
# user_name = 'yanzan'
# password = '123'

# tag = True
# while tag:
#     name = input("请输入您的账号：")
#     pwd = input("请输入您的密码：")
#
#     if name == user_name and pwd == password:
#         print("账号密码登陆成功")
#         tag = False
#     else:
#         print("账号名或密码错误,请重新输入")


# 4、while循环退出的两种方式
# 方式一：将条件改成假
'''
user_name = 'yanzan'
password = '123'

tag = True
while tag:
    name = input("请输入您的账号：")
    pwd = input("请输入您的密码：")

    if name == user_name and pwd == password:
        print("账号密码登陆成功")
        tag = False
    else:
        print("账号名或密码错误,请重新输入")
'''

# 方式2：while+break： break是终止的意思，运行到break就立刻结束本次循环！！！ break简单粗暴-本层循环
'''
user_name = 'yanzan'
password = '123'

while True:
    name = input("请输入您的账号：")
    pwd = input("请输入您的密码：")

    if name == user_name and pwd == password:
        print("账号密码登陆成功")
        break
    else:
        print("账号名或密码错误,请重新输入")

    print('======end======')
'''

# 5、while循环的嵌套
# while True:
#     print("hello world")
#     while True:
#         print("hello world")
#         break
#         while True:
#             print("hello world2")
#             break

"""
user_name = "yanzan"
user_password = "pwd123"

while True:
    name = input("请您输入您的用户名：")
    pwd = input("请您输入您的密码：")
    if name == user_name and pwd == user_password:
        print("恭喜您，登陆成功！！！")
        while True:
            cmd = input("请您输入命令：")
            if cmd == 'q':
                print("退出成功！")
                break  # 结束本层的while循环
            else:
                print("正在运行{c}命令中......".format(c=cmd))
        break  # 结束本层的while循环
    else:
        print("账号密码错误，请重新尝试！！！")
"""  # 本代码有一个问题，就是如果while循环的嵌套多了之后，都需要写一个break跳出本次循环。如果有100个 那就需要写100个break跳出循环

# 6、while + break
#
# user_name = "yanzan"
# user_password = "pwd123"
#
# while True:
#     name = input("请您输入您的用户名：")
#     pwd = input("请您输入您的密码：")
#     if name == user_name and pwd == user_password:
#         print("恭喜您，登陆成功！！！")
#         while True:
#             cmd = input("请您输入命令：")
#             if cmd == 'q':
#                 print("退出成功！")
#                 break  # 结束本层的while循环
#             else:
#                 print("正在运行{c}命令中......".format(c=cmd))
#         break  # 结束本层的while循环
#     else:
#         print("账号密码错误，请重新尝试！！！")
# """ # 本代码有一个问题，就是如果while循环的嵌套多了之后，都需要写一个break跳出本次循环。如果有100个 那就需要写100个break跳出循环


# 7、while + contiue：contiue也是结束循环的意思，这个是结束本次循环，直接进入下次的循环
# count = 0
# while count < 6:
#     if count == 4:
#         count += 1
#         print("现在开始跳出")
#         continue # 直接进入下次的循环  跳出本次循环直接进入下次循环，break是直接退出本次循环结束。 contiue后续的所有代码不在运行
#     print(count)
# count += 1

# 注意：在continue之后添加同级别代码是毫无意义的，因为它会直接进入下次循环，将永远无法运行后续同级别代码

# while True:
#     if True:
#         print("aaaaa")
#         continue
# 需要记住一点就是continue就是结束本次循环直接进入下次循环！

# 8、while + else 只有在while循环当中break打断之后就不会运行。
# count = 0
# while count < 6:
#     print(count)
#     count += 1
#     break
# else:
#     print("else 包含的代码会在while循环结束之后，并且while循环是在没有被break打断的情况下正常结束掉的循环才会运行else后的代码")
# else就是针对break的，continue没事
