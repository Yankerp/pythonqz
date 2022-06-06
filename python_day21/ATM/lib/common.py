# -*- coding utf-8 -*-

"""
@author:yankerp
@url:www.yankerphub.com
"""

import os
import sys

import time

BASE_DIR = os.path.dirname(os.path.dirname(__file__))
print(BASE_DIR)
LOG_PATH = r"{LOG_PATH}/log/user.log".format(LOG_PATH=BASE_DIR)


def logger(next):
    with open(LOG_PATH, mode='at', encoding='utf-8') as f:
        f.write("{time}-{next}\n".format(time=time.strftime("%Y-%m-%d %H:%M:%S"), next=next))
