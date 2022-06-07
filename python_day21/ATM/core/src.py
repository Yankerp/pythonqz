# -*- coding utf-8 -*-

"""
@author:yankerp
@url:www.yankerphub.com
"""


import sys
from lib.common import logger

def exit():
    print("退出程序成功")
    logger('开始执行退出程序')
    sys.exit()


def login():
    print("登录功能")
    logger('开始执行登录程序')


def register():
    print("注册功能")
    logger('开始执行注册程序')


def witdraw():
    print("提现功能")
    logger('开始执行提现程序')


def transfer():
    print("转账功能")
    logger('开始执行转账程序')


def run():
    print("run".center(50, "*"))
    print(sys.path)
    while True:
        user_caidan = {
            "1" : ["退出功能", exit],
            "2" : ["登录功能", login],
            "3" : ["注册功能", register],
            "4" : ["提现功能", witdraw],
            "5" : ["转账功能", transfer]
        }

        for k in user_caidan:
            print(k, user_caidan[k][0])

        your_input = input("请选择：").strip()

        if your_input in user_caidan:
            user_caidan[your_input][1]()
        else:
            print("输入的不存在！！！")
            logger("输入的指令不存在")




if __name__ == '__main__':
    run()