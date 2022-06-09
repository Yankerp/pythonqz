# -*- coding utf-8 -*-

"""
@author:yankerp
@url:www.yankerphub.com
"""

# 这是执行命令的模块
import subprocess

# 如果命令正确就弄进管道
res = subprocess.Popen('dir', shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)

zhengq = res.stdout.read() # 正确结果
cuowu = res.stderr.read() # 错误结果
# print(zhengq.decode('GBK'))  # 系统的编码格式
# print(cuowu)

