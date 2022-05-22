# -*- coding utf-8 -*-

"""
@author:yankerp
@url:www.yankerphub.com
"""


import time
with open('access.log', mode='rb') as f:
    f.seek(0, 2)
    while True:
        res = f.readline()
        if len(res) == 0:
            time.sleep(0.5)
        else:
            print(res.decode('utf-8'))