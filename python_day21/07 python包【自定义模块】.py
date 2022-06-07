# -*- coding utf-8 -*-

"""
@author:yankerp
@url:www.yankerphub.com
"""

'''
1、什么是包
    包就是一个包含有__init__文件的文件夹
        


2、为何要有包
    包的本质就是模块的一种形式，包是用来被当做模块导入的



'''
# 1、产生一个名称空间
# 2、运行包下的__init__.py文件，运行py文件将运行过程中产生的名字，都丢到1的名称空间中
# 3、在当前执行文件名称空间中拿到一个名字，该名字是指向1的名称空间
# import mmm  # mmm----->指向init
# print(mmm.x)
# print(mmm.y)
# mmm.say()


# fuu模块的使用者！
import sys

print(sys.path)
import fuu  # fuu.__init__文件

fuu.f1()
fuu.f2()
fuu.f3()
fuu.f4()

# 强调：
"""
1、无论是import还是from...import导入的时候带 "." 那么"."的左边必须是一个包，语法规定！
    例如：from a.bin.c.d.e.f import xxx  其中a.bin.c.d.e这几个都必须是包
    
2、如果两个包内有相同名字的两个模块，是不会冲突的，没有任何影响
3、import 导文件时文件来源于模块.py文件，import导入包的时候就是在导入包下的___init__.py文件
"""

# 总结：包内的导入推荐使用相对导入，对模块的设计者的建议，相对导入不能跨不出包，所以相对导入仅限于包内的模块彼此之间闹着玩
# 总结：更加通用的方式就是绝对导入，绝对导入是没有任何限制的，所以绝对导入是一种通用的导入方式

# 总结: os.path.dirname是获取当前所在文件的父级目录的文件夹，__file__是获取当前文件名的绝对路径
# So，通过os.path.dirname(__file__) 就可以获取到当前文件的父级目录的文件夹名称，从而通过sys.path.append() 加入到环境变量，实现绝对导入
