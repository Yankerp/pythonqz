# -*- coding utf-8 -*-

"""
@author:yankerp
@url:www.yankerphub.com
"""

count = 0
while count < 6:
    with open('access.log', mode='rt', encoding='utf-8') as f1:
        with open('accesszz.log', mode='at', encoding='utf-8') as f2:
            for line in f1:
                print(len(line))
                f2.write(line)
                count += 6
