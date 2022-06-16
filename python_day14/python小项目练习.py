# -*- coding utf-8 -*-
import os
import time

user_database = r"D:\pythonqz\python_day14\databse.txt"


def welcome():
    while True:
        print("欢迎来到网站系统".center(60, "*"))
        print("""
        1、登录APP
        2、注册APP
        q、退出程序
        """)
        your_num = input("请输入：").strip()
        if your_num == "1":
            user_login()
        elif your_num == "2":
            receive_user_input()
        elif your_num == "q":
            print("退出成功")
            break
        else:
            print("输入不合法，请重新输入！！！")


def os_path():
    if os.path.exists(user_database):
        return True
    else:
        with open(user_database, mode='xt', encoding='utf-8') as f:
            f.write('username:password\n')
            f.close()
        return 'ok'


def user_input():
    while True:
        your_name = input("请您输入您的用户名：").strip()
        your_pwd = input("请您输入您的密码：").strip()

        if your_name == '' or your_pwd == '':
            print('用户名或密码不能为空，请重新输入！！！')
        else:
            return your_name, your_pwd


def receive_user_input():
    """用户注册"""
    while True:
        if os.path.exists(user_database):
            name, password = user_input()
            with open(user_database, mode='at', encoding='utf-8') as f2:
                f2.write("{name}:{password}\n".format(name=name, password=password))
                print("注册成功您的账号是{name},密码是{password}".format(name=name, password=password))
            your_xuanze = input("是否需要直接登录？yes/no：").strip()
            if your_xuanze == 'yes':
                user_login()
                break
            else:
                welcome()
                return 'exit'


def user_login():
    print("欢迎来到登录系统，以下输入登录系统的账户名密码".center(50, "*"))
    count = 0
    while count < 3:
        name, password = user_input()
        with open(user_database, mode='rt', encoding='utf-8') as f:
            for x in f:
                res = x.strip()
                result = res.split(":")

            if result[0] == name and result[1] == password:
                print("账号密码正确，登录成功！！！------后续直接跳转到登录页面.........")
                break
            else:
                print("账号或密码错误，请您输入正确的账号或者密码！！！")
                count += 1


def result():
    res = os_path()
    if res == True or res == 'ok':
        welcome()
        return 0


result()
