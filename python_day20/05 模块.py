# -*- coding utf-8 -*-

"""
@author:yankerp
@url:www.yankerphub.com
"""

"""
一、什么是模块？
    模块就是一系列功能的集合体分为三大类：
        1、内置模块用C语言编写的一些模块
        2、第三方的模块
        3、自定义的模块，就是自己定义写的一些模块
            一个python文件本身就是一个模块文件名叫 m.py  模块名叫：m

二、为何要有模块？
    1、内置与第三方的模块拿来就用，不需要定义，这种拿来主义可以极大的提升自己的开发效率
    2、自定义模块
        可以将程序的各部分功能提取出来放到一个模块当中，为大家共享使用
        好处是减少了代码冗余，程序结构更加清晰
        
三、如何使用模块
"""
import foo

# 首次导入模块会发生？？
# 1、执行foo.py
# 2、会产生foo.py的名称空间，将foo.py运行g过程中产生的名字都丢到了foo的名称空间当中
# 3、在当前文件中产生一个名字叫做foo，该名字指向2中的名称空间

# 之后的导入,都是直接引用首次导入产生的foo的名称空间，不会重复执行代码
# import foo
# import foo
# import foo
# import foo
# import foo

# 2、引用：
# print(foo.func())
# 强调1：模块名.名字是指名道姓问某一个模块要名字对应的值，不会与当前名称空间中的名称发生冲突

# def func():
#     print("haaaaa")
#
# foo.func()


# 强调2：无论是查看还是修改，操作的都是原文件模块本身，与调用位置无关
# import foo

# 3、可以在一行用,号分割可以导入多个模块
# import time,foo,  # 但是不建议这么做


# 4、导入模块的规范：
"""
1、python的内置模块
2、第三方的模块
3、程序员自己定义的模块
"""

# 5、import .... as ......
# import foo as niubi  # 把foo的内存地址给了niubi，相当于起了一个别名
# niubi.func()
# 当模块名非常长的情况下，那么可以用as 别名一下子~~~~~~~~


# 6、模块是第一类对象
# import foo

# 7、自定义的模块应该采用纯小写+下划线的方式，和变量名一样

# 8、可以在函数内导入模块
# def yankerp():
#     import foo  #










