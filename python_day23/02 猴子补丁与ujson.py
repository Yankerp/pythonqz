# -*- coding utf-8 -*-

"""
@author:yankerp
@url:www.yankerphub.com
"""

import json
import ujson  # 和json一样，但是比json更快


def monkey_patch_json():
    json.dumps = ujson.dumps
    json.loads = ujson.loads


monkey_patch_json()

# 以上的执行需要在执行文件操作，这样其他的关联的文件代码都可以引用到

# json.dumps=其他的更好的dumps功能替换json.dumps功能
# json.loads=其他的更好的dumps功能替换json.loads功能
