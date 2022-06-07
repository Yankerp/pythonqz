# -*- coding utf-8 -*-

"""
@author:yankerp
@url:www.yankerphub.com
"""
import os


def check_mysql_status():
    mysql_status = os.popen('netstat -anpt | grep mysqld | wc -l')
    code = mysql_status.readline().strip()
    return code


def restart():
    status_code = check_mysql_status()
    if status_code == "0":
        print("无法检测到MySQL的进程，正在重启......")
        os.system('/etc/init.d/mysqld start')
        status_code2 = check_mysql_status()
        if status_code2 == "0":
            print("重启MySQL失败！！！！！")
        else:
            print("重启MySQL成功！！！！")
    else:
        print("MySQL正常运行......")

if __name__ == '__main__':
    restart()