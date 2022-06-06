# -*- coding utf-8 -*-

"""
@author:yankerp
@url:www.yankerphub.com
"""

import os
import sys
sys.path.append(os.path.dirname(os.path.dirname(__file__)))
from core import src

print("start.py".center(100, "*"))
print(sys.path)
src.run()
