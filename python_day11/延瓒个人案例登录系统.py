# -*- coding utf-8 -*-

"""
@author:yankerp
@url:www.yankerphub.com
"""

count = 0
while count < 3:
    print("欢迎来到程市注册登录系统， 1-登录   2-注册   q-退出系统".center(50, "*"))
    your_xx = input("请您输入选项：").strip()
    if your_xx == '1':
        print('欢迎来到登录系统'.center(50, '*'))
        your_login_name = input("请您输入登录用户名：").strip()
        your_login_password = input("请您输入登录密码：").strip()
        if len(your_login_name) == 0 and len(your_login_password) == 0:
            print("您的输入为空，不能输入空的内容请重新输入")
            # print("请您输入正确的用户名和密码,还剩于{s}次机会".format(s=count))
        else:
            with open('/Users/ayao/PycharmProjects/pythonqz/python_day11/database.txt', mode='rt',
                      encoding='utf-8') as f:
                for test in f:
                    tun, tup = test.strip().split(":")
                    if your_login_name == tun:
                        # 走到这一步一定是用户名存在！
                        with open('/Users/ayao/PycharmProjects/pythonqz/python_day11/database.txt', mode='rt',
                                  encoding='utf-8') as f1:
                            for x in f1:
                                user_name, user_password = x.strip().split(":")
                                if your_login_name == user_name and your_login_password == user_password:
                                    print("程尧登录成功啦，么么么哒！！！！")
                                    print("支付宝到账100元，请登录程尧支付宝查收")
                                    break
                            else:
                                print("账号密码错误，登录失败！！！")
                                count += 1
                                break
                            break
                else:
                    print("账号不存在请您滚去注册！！！")
    elif your_xx == '2':
        print('欢迎来到注册系统'.center(50, '*'))
        while True:
            your_name = input("请您输入注册用户名：").strip()
            your_password = input("请您输入注册密码：").strip()
            if len(your_name) == 0 and len(your_password) == 0:
                print("请输入需要注意的用户名和密码，不能为空")
            else:
                with open('/Users/ayao/PycharmProjects/pythonqz/python_day11/database.txt', mode='rt',
                          encoding='utf-8') as f:
                    for x in f:
                        un, up = x.strip().split(":")
                        if your_name == un:
                            print("对不起，此用户名已经注册，你特码的不能注册. 请你重新注册")
                            break
                        else:
                            print("注册成功，你的用户名是{name},你的密码是{pwd}".format(name=your_name, pwd=your_password))
                            with open('/Users/ayao/PycharmProjects/pythonqz/python_day11/database.txt', mode='at',
                                      encoding='utf-8') as f:
                                f.write('{name}:{pwd}\n'.format(name=your_name, pwd=your_password))
                                print("写入数据库成功......")
                            break
            break
    elif your_xx == 'q':
        print("退出系统成功，再见!!".center(50, "*"))
        break
    else:
        print("输入不正确，重新输入！")
        count += 1
else:
    print("你已经输错3次和一个傻逼一样!!!!")
