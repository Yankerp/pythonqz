# -*- coding utf-8 -*-

"""
@author:yankerp
@url:www.yankerphub.com
"""


# 一、形参与实参的介绍：
# 形参：在定义函数的阶段定义的参数称之为形式参数，简称为形参，形参相当于变量名
def func(name, password):
    print(name, password)


# func('yanzan', 'pwd123.com')

# 实参：就是在调用函数的阶段传入的值，称之为叫实际参数，简称为实参。实参相当于变量值呗。

# 形参与实参的关系是什么？
"""
1、首先在定义阶段两者没有关系，但是在调用阶段，实参的值会赋值给形参. ----->变量值赋值给了变量名
2、这种绑定关系只能用于函数体内，只能在函数体内使用 
3、实参与形参只有在调用的时候生效，当调用结束之后解除绑定关系
"""


# 2、形参与实参的具体使用
# 2.1、位置参数：按照从左到右的顺序依次定义的参数称为位置参数
# 位置定义的形参：在函数定义阶段！！按照从左到右的位置定义的"形参"变量名
#       特点：必须被传值，多一个不行，少一个也不行。
# def func(x, y):
#     print(x, y)


# func(1, 2, 3)
# func(1,)
# func(1, 2)

# 位置定义的实参：在函数调用阶段！！！按照从左到右的顺序依次传入的值
#   特点：按照顺序与形参一一对应
# func(1, 2)  # 顺序就是1给了x 2给了y
# func(2, 1)  # 顺序就是2给了x 1给了y

# ====================================================================================
# 2.2、关键字参数
# 关键字实参：在函数调用阶段，按照key=value的形式传入值,
#   特点：指名道姓的给某个形参传值，可以完全不参照顺序
# def func(x, y):
#     print(x, y)

# func(x=1, y=2)

# 补充：关键字实参与位置实参的混合使用
# 1、位置实参必须放在关键字实参之前使用，这个是oython规定的语法格式
# func(2, y=1)
# 2、不能为同一个形参重复的传值
# func(1, y=2, x=3)  # TypeError: func() got multiple values for argument 'x'

# ====================================================================================
# 2.3、默认参数
# 默认形参：在定义函数阶段就已经被赋值的形参称之为默认参数，或者叫默认形参
#       特点：在定义阶段就已经为其赋值，意味着在调用阶段可以不用为其赋值，但是要赋值也可以赋，可以赋值也可以不用赋值
# def func(x=3, y=3):
#     print(x, y)
#
# func() # 可以不用为其赋值
# func(x=10, y=20) # 也可以为其赋值

# ====================================================================================
# 补充：位置形参与关键字形参的混合使用
# 1、位置的形参必须要在关键字形参的前面
def func(name, password='pwd123'):
    print(name, password)


# 2、默认形参的值是在定义阶段被赋值的，准确的说被赋予的是值得内存地址
def func(x, y=2 + 2):  # y的默认形参是在函数定义的时候被赋值的
    print(x, y)


# func(1)

# 3、虽然默认值可以指定为任意的数据类型，但是不推荐使用可变类型
# 函数的定义应该遵循一个原则：调用可以预知到靠谱的结果，预知到结果




# ====================================================================================




# 2.4、可变长度的参数（*与 ** 的用法）
# 可变长度指的是在调用函数时，传入的值（实参）个数不固定
# 而实参是用来为形参赋值的，所以对应着,针对溢出多出来的实参必须有对应的形参来接收

# 2.4.1、可变长度的位置参数
# I:*形参名：用来接收溢出多余的实参，溢出多余的位置都是会被*保存成元组的格式，然后将元组赋值给紧跟其后的形参名
# *后面跟的是一个变量名，就是一个普通的名字，跟的可以是任意的名字，但是python约定俗成应该写成args
# def func(x, y, *z):
#     print(x,y,z)

# func(1,2,3,4,5,6,7,8)

def my_sum(*args):  # 通常将这个*后面的那个字母写成args，args就是一个变量名，没别的意思。
    count = 0
    for i in args:
        count += i
    return count


# res = my_sum(1,2,3,4,5,6,7,8,8,9,0,)
# print(res)

# II：*可以也可以用在实参中,实参中带*，先将*后的值打散成位置实参
def func(x, y, z):
    print(x, y, z)


# func(1,2,3)
# func(*[111,222,333])  # func(111,222,333)

# III：形参与实参中都带*
def func(x, y, *args):
    print(x, y, args)


# func(1,2,[3,4,5,6,7])
# func(1,2,*[3,4,5,6,7])


# 2.4.2、可变长度的关键字参数
# I: **形参名：用来接收溢出多余的关键字实参，**会将溢出多余的关键字实参保存成字典的格式,然后赋值给**后面的形参名
#       **后面的形参名可以是任意的名字，但是python约定俗成应该是kwargs
def func(x, y, **kwargs):
    print(x, y, kwargs)


# func(1,2,name="yanza", password='owd123.com')

# II:**可以也可以用在实参中,实参中带**，先将**后的值打散成关键字实参,**后跟的只能是字典
def func(x, y, z):
    print(x, y, z)

# func(*{'x':"yx", 'y':'yz', 'z':'yzzzz'})
# func(**{'x':"yx", 'y':'yz', 'z':'yzzzz'})
# func(**{'x':"yx", 'y':'yz', 'z':'yzzzz'})

## III：形参与实参中都带**
# def func()


# **和*混合用法    *args必须要在**kwargs之前


# 2.5、命名关键字参数（了解）
# 2.6、组合使用（了解）
