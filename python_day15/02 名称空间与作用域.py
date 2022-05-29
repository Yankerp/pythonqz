# -*- coding utf-8 -*-

"""
@author:yankerp
@url:www.yankerphub.com
"""

# 一、名称空间（namespaces）：存放名字的地方，是对内存栈区的划分
# 有了名称空间之后，就可以在栈区中存放相同的名字了，名称空间分为三种
# 三种名称空间
# 1.1、内置名称空间
# 存放的名字：存放的是python解释器内置的名字
"""
>>> print
<built-in function print>
>>> input
<built-in function input>
>>> 
"""
# 存活周期：当python解释器启动的时候产生内置名称空间、当python解释器关闭的时候结束内置名称空间。


# 1.2、全局名称空间
# 存放的名字：只要不是函数内定义的名字并且也不是内置的，剩下的都是全局名称空间名字！！！ 这个需要好好理解
# 存活周期：python文件执行则产生，python文件关闭则销毁
# x = 10
import os

# if 17 < 111:
#     y = 20
#     if 3 == 3:
#         z = 30


# func = '函数的内存地址'
# def func():  # func本身名字就是属于全局名称空间
#     a = 111
#     b = 222


# Fuu = '类的内存地址'
# class Fuu:
#     pass


# 1.2、局部名称空间
# 存放的名字：一切凡是在调用函数代码运行过程中所产生的名字都可以称为局部名称空间
# 生命周期：当函数调用的时候所产生局部名称空间，当函数结束之后就会销毁
#
# def func():
#     name = 'yanzan'


# func()  # 调用函数代码运行的过程当中局部名称生效

# 注意：同一个函数调用多少次，就会产生开辟多少次的局部名称空间


# 1.4、名称空间的加载顺序是什么？
# 内置名称空间——>全局名称空间——>局部名称空间


# 1.5、销毁顺序
# 局部名称空间——>全局名称空间——>内置名称空间销毁

# 1.6 名字名称的查找优先级
# 大的原则的是从当前所在的位置向上一层一层的查找。
"""
内置名称空间
全局名称空间
局部名称空间
"""


# 例如当前在局部空间，那么查找顺序就是局部名称空间----->全局名称空间----->内置名称空间
# input = 'yanzan'
#
# def func():
#     input = 'zhangsan'
#     print(input)
#
# func()

# 例如当前在全局空间，那么查找的循序就是全局名称空间------>内置名称空间

# input = 'yanzan'

# def func():
#     input = 'zhangsan'
#     # print(input)


# func()

# print(input)  # 当前的位置是在全局的空间查找这个input的名称， 如果全局空间有这个名字的话就可以了，如果没有的话会去内置空间查找

'''以上的代码完全可以解释名称空间的查找顺序'''


# 示范1：

# def func():
#     print(x)
#
# func()
# x = 111




# # 示范2：名称空间的嵌套是以函数定义的阶段为准则，与在哪里调用无关
# x = 111
# def func1():
#     print(x)
#
# def func2():
#     x = 222
#     print(x)
#     func1()
#
# func2()





# 示范3：函数的嵌套定义：
# input = 1111

# def func1():
#     # input = 2222
#     def func2():
#         # input = 3333
#         print(input)
#
#     func2()
#
# func1()


# input = 1111
def func1():
    # input = 222222
    def func2():
        # input = 333333333
        def func3():
            print(input)

        func3()
    func2()

# func1()


# def func1():
#     def func2():
#         # name = 'zhangsan'
#         print(name)
#     name = 'yanzan'
#     func2()
# func1()


# 示范4：

# x = 10
# def func1():   # 变量先定义后引用
#     print(x)
#     x = 222
#
# func1()


# 二、作用域-作用范围
# 作用域就是 全局作用域和局部作用域
# 全局作用域：（内置名称空间、全局名称空间）
# 1、全局存活
# 2、全局有效：被所有的函数共享所有的代码共享
# x = 111
#
# def func():
#     print(x, id(x))
#
# def func2():
#     print(x, id(x))
#
# func()
# func2()



# 局部作用域：局部空间名称的名字
# 1、临时存活，函数调用时活一下，不调的时候就死了
# 2、局部有效，只能在函数内使用
#
# def func():
#     x = 111
#     print(x)




# LEGB---> local---》global  built-in


# built-in
# Global
def f1():
    # ENCLOSING
    def f2():
        # ENCLOSING
        def f3():
            # local
            pass
















