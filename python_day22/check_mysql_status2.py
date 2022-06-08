# -*- coding: utf-8 -*-

"""这是python2版本的MySQL检测脚本"""
# 钉钉推送
import os
import json
import time
import requests
import hmac
import hashlib
import base64
import socket
import urllib
# import urllib.parse


# def mysql_process():
#     mysql_status = os.popen('netstat -anpt | grep mysqld | wc -l')
#     code = mysql_status.readline().strip()
#     return code
#
#
# def check_mysql_status():
#     status_code = mysql_process()
#     if status_code == "0":
#         print("无法检测到MySQL的进程，正在重启......")
#         os.system('/etc/init.d/mysqld start')
#         status_code2 = mysql_process()
#         if status_code2 == "0": # 重启失败了.......
#             dingding(webhook, secret, dingding_text="未能检测到MySQL服务，尝试重启失败，请及时查看！！！")
#         else:
#             print("重启MySQL服务成功，MySQL正常运行中！！！！")
#             dingding(webhook, secret, dingding_text="未能检测到MySQL服务，尝试重启成功，MySQL正在运行....")


def dingding(webhook, secret, dingding_text):
    # 获取当前主机的IP地址
    host_ipaddr = socket.gethostbyname(socket.gethostname())
    hostname = socket.gethostname()
    timestamp = str(round(time.time() * 1000))
    secret_enc = secret.encode('utf-8')
    string_to_sign = '{}\n{}'.format(timestamp, secret)
    string_to_sign_enc = string_to_sign.encode('utf-8')
    hmac_code = hmac.new(secret_enc, string_to_sign_enc, digestmod=hashlib.sha256).digest()
    sign = urllib.quote_plus(base64.b64encode(hmac_code))
    url = '%s&timestamp=%s&sign=%s' % (webhook, timestamp, sign)

    headers = {'Content-Type': 'application/json'}
    data = {
        "msgtype": "text",
        "text": {"content": """
        服务器IP地址：{host_ipaddr}
        服务器主机名：{hostname}
        内容：{dingding_text}
        """.format(host_ipaddr=host_ipaddr, dingding_text=dingding_text, hostname=hostname)},
        "at": {
            "atMobiles": [
                ""  # 需要艾特的人的手机号
            ],
            "isAtAll": 0  # 是否艾特全体成员
        }
    }

    res = requests.post(url, data=json.dumps(data), headers=headers)

    if res.json()['errmsg'] == 'ok':
        print("钉钉告警发送成功！！！！")



webhook = ''
secret = ''

dingding(webhook, secret, dingding_text="未能检测到MySQL服务，尝试重启成功，MySQL正在运行....")
