# -*- coding utf-8 -*-

"""
@author:yankerp
@url:www.yankerphub.com
"""

import sys
import shutil

old_new_file = sys.argv
shutil.copy(old_new_file[1], old_new_file[2])
