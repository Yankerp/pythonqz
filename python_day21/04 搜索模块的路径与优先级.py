# -*- coding utf-8 -*-

"""
@author:yankerp
@url:www.yankerphub.com
"""

# 无论是import还是from import在导入的时候都涉及到查找文件模块路径的问题：
# 优先级：
# 1、首先查找顺序是先从内存去找
# 2、内存没有的话就从硬盘找：按照sys.path环境变量中存放的文件夹的顺序依次查找要导入的模块


# import sys
# import fuu

# print(sys.path)  # sys.path里面存放了模块查找的路径，准确来说是当前执行文件所在目录，存放了很多的文件夹


# 其中第一个文件夹是当前执行文件所在的文件夹
# 第二个文件夹就是当前项目所在的文件夹，这个第二个值是pycharm帮我们加的，所以可以当第二个文件夹不存在


# 验证一个模块的导入是先从内存找后从硬盘找...... 代码实现：


# 补充：在sys模块当中有个功能叫做：sys.modules可以查看当前内存当中已经加载到内存当中的模块
# print('fuu' in sys.modules)
# print(sys.modules)






import sys

# 找foo就把foo的文件夹添加到环境变量当中
sys.path.append(r"E:\pythonqz-master\python_day21\test")  # 临时加
import foo








