# -*- coding: utf-8 -*-

"""这是python3版本的MySQL检测脚本"""

import json, time, requests, hmac, hashlib
import base64
import urllib.parse
import paramiko


class MySQL_Status:
    def __init__(self, hostname, port, username):
        self.hostname = hostname
        self.port = port
        self.username = username
        self.send_out_time = time.strftime("%Y-%m-%d %H:%M:%S")

    def connect_server(self, shellbash: str) -> str:
        ssh = paramiko.SSHClient()
        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        ssh.connect(hostname=self.hostname, port=self.port, username=self.username, key_filename='/root/.ssh/id_rsa')
        stdin, stdout, stderr = ssh.exec_command(shellbash)  # 执行远程命令
        result = stdout.read()
        result = result.decode('UTF-8').strip("\n")
        return result

    def check_mysql_process(self):
        """检测mysql进程"""
        res = self.connect_server('netstat -anpt | grep mysqld |wc -l')
        return res

    def check_mysql_restart(self):
        """重启mysql进程"""
        self.connect_server('/etc/init.d/mysqld restart')

        restart_status_code = self.check_mysql_process()
        return restart_status_code

    def check_mysql_status(self, status_code):
        if status_code == "0":
            print(f"无法检测到MySQL的进程，正在重启.....")
            restart_code = self.check_mysql_restart()
            if restart_code == "0":
                print("未能检测到MySQL服务，尝试重启MySQL失败，请及时查看！！！")
                self.dingding(webhook, secret, dingding_text="未能检测到MySQL服务，尝试重启MySQL失败，请及时查看！！！")
            else:
                print("重启MySQL服务成功，MySQL正常运行中！！！！")
                self.dingding(webhook, secret, dingding_text="未能检测到MySQL服务，尝试重启成功，MySQL正在运行....")
        else:
            print("MySQL正常运行中.....")

    def dingding(self, webhook, secret, dingding_text):
        # 获取当前主机的IP地址
        host_ipaddr = self.hostname
        timestamp = str(round(time.time() * 1000))
        secret_enc = secret.encode('utf-8')
        string_to_sign = '{}\n{}'.format(timestamp, secret)
        string_to_sign_enc = string_to_sign.encode('utf-8')
        hmac_code = hmac.new(secret_enc, string_to_sign_enc, digestmod=hashlib.sha256).digest()
        sign = urllib.parse.quote_plus(base64.b64encode(hmac_code))
        url = '%s&timestamp=%s&sign=%s' % (webhook, timestamp, sign)

        headers = {'Content-Type': 'application/json'}
        data = {
            "msgtype": "text",
            "text": {"content": """
            服务器IP地址：{host_ipaddr}
            时间：{send_out_time}
            内容：{dingding_text}
            """.format(host_ipaddr=host_ipaddr, send_out_time=self.send_out_time, dingding_text=dingding_text)},
            "at": {
                "atMobiles": [
                    ""  # 需要艾特的人的手机号
                ],
                "isAtAll": 0  # 是否艾特全体成员
            }
        }

        res = requests.post(url, data=json.dumps(data), headers=headers)

        if res.json()['errmsg'] == 'ok':
            print("钉钉发送告警成功.......")


webhook = ''
secret = ''

if __name__ == '__main__':
    result = MySQL_Status(hostname='', port='', username='')
    code = result.check_mysql_process()
    result.check_mysql_status(code)
