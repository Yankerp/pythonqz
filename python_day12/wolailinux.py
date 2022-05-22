# -*- coding utf-8 -*-

"""
@author:yankerp
@url:www.yankerphub.com
"""

import time
with open('wolai.log', mode='rb') as f:
    f.seek(0, 2)
    num = f.tell()
    print("现在的指针是在{num}".format(num=num))
    while True:
        res = f.readline()
        if len(res) == 0:
            time.sleep(1)
        else:
            print(res.decode('utf-8'),end="")
