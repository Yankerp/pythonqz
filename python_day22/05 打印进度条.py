# -*- coding utf-8 -*-

"""
@author:yankerp
@url:www.yankerphub.com
"""

# 进度条，动态效果
# [#      ] 1%
# [##     ] 2%
# [###    ] 3%
# [####   ] 4%
# [#####  ] 5%

# print('[%-50s]' %'#' )# 左对齐，宽度为50
import time

# res = ''
# for i in range(50):
#     res+="#"
#     time.sleep(0.5)
#     print('\r[%-50s]' % res, end='' )


# print("this is a %s" %'yanzan')

# print('[%-50s]' %'#')

res = ''

# for count in range(50):
#     if user_download < file_size:
#         user_download += 1024
#         user_size = user_download / file_size * 100
#         res += '#'
#         time.sleep(0.2)
#         print('\r[%-50s] %s %%' %(res, int(user_size)), end='')

user_download = 1024
file_size = 1212121



while user_download < file_size:
    user_download += 1024
    time.sleep(0.001)
    # 求百分比数字：
    baifenbi = user_download / file_size

    # 算进度条
    jinfutiao = int(100 * baifenbi) * "#"

    print('\r[%-100s] %s%%' % (jinfutiao, int(100*baifenbi)), end='')
