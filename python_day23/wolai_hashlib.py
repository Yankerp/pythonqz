# -*- coding utf-8 -*-

"""
@author:yankerp
@url:www.yankerphub.com
"""

import hashlib

# res = hashlib.md5()
# res.update('yankerp'.encode('utf-8'))
# print(res.hexdigest())  # 527a70e5cb1b74140bab3579c107920c


# res = hashlib.md5()
# res.update('yankerp'.encode('utf-8'))
# print(res.hexdigest())    # 527a70e5cb1b74140bab3579c107920c

import hashlib


def zhuce():
    your_name = input("请输入你的名字：").strip()
    your_password = input("请输入您的密码：").strip()
    password = hash_b(your_password)
    with open('database.txt', mode='at', encoding='utf-8') as f:
        f.write("{name}:{password}\n".strip('').format(name=your_name, password=password))


def login():
    your_name = input("请您输入您的用户名：").strip()
    your_password = input("请您输入您的密码：").strip()

    with open('database.txt', mode='rt', encoding='utf-8') as f:
        for name in f:
            userinfolist = name.strip().split(':')
            userinfopwd = hash_b(your_password)
            if your_name == userinfolist[0] and userinfopwd == userinfolist[1]:
                print("登录成功")
                return 'ok'
        else:
            print("账号密码错误....")



def hash_b(pwd):
    res = hashlib.md5()
    res.update(pwd.encode('utf-8'))
    pwd_hash = res.hexdigest()
    return pwd_hash

# zhuce()
login()