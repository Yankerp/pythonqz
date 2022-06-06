# 1、绝对导入以包的文件夹作为起始导入：绝对导入绝对不会出现任何问题
# from fuu.m1 import f1
# from fuu.m2 import f2
# from fuu.m3 import f3
# from fuu.bbb.m4 import f4


# 2、相对导入:只能在仅限于包内使用，不能跨出包
# . 代表当前文件夹
# .. 代表上层文件夹

from .m1 import f1
from .m2 import f2
from .m3 import f3
from .bbb.m4 import f4