# -*- coding utf-8 -*-

"""
@author:yankerp
@url:www.yankerphub.com
"""


import time
import foo # 首先先从硬盘当中查找也就是sys.path中存在的文件夹依次查找有么有foo

# time.sleep(10) # 当foo导入到内存后等待10秒，删除foo模块


print("开始第二次的导入")
import foo # 删除后再次导入foo，这个时候就从内存导入，而不是硬盘。 验证了模块如果在内存当中存在是先从内存导入

import sys
res = sys.modules
for i in res:
    print(i)