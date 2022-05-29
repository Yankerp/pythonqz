# -*- coding utf-8 -*-

"""
@author:yankerp
@url:www.yankerphub.com
"""

# 一、大前提
"""
3、闭包函数 = 名称空间与作用域 + 函数嵌套 + 函数对象， 这三个知识点的综合应用。不是新的知识点
核心点：名字的查找关系是以函数定义阶段为准
"""


# 二、什么是闭包函数
# "闭"函数指的是该函数是内嵌函数
# "包"函数指的是该函数包含对外层函数作用域名字的引用（不是对全局作用域）

# 闭包函数之名称空间与作用域+函数嵌套的应用
def f1():
    name = 'yanzan'

    def f2():  # 此时f2就是闭函数
        print(name)  # 当闭函数调用了外层函数作用域名字的引用就是闭包函数，此时就是闭包函数


# 以后无论f2在哪里调用，它的包永远都是f1的包，定义的yanzan，不会有任何改变，除非f1这个包的定义改变


# 闭包函数：函数对象
def f1():
    x = 3333333333333

    def f2():
        print(x)

    return f2  # 返回f2的内存地址

res = f1()
print(res)  # <function f1.<locals>.f2 at 0x7f86a11b91f0>

res()







# 四、闭包函数的应用场景，学会了新的一种为函数传递参数的方式！！！！！
# 方式1：
# import requests
# def get(url):
#     res = requests.get(url)
#     print(len(res.text))
#
# get('https://www.baidu.com')
# get('https://www.csdn.net')
# get('https://zhuanlan.zhihu.com/p/401129069')


# 方式二：
import requests
def get_url(url):
    url = url
    def get():
        res = requests.get(url)
        print(len(res.text))
    return get

baidu = get_url('https://www.baidu.com')
baidu()

csdn = get_url('https://www.csdn.net')
csdn()

zhihu = get_url('https://zhuanlan.zhihu.com/p/401129069')
zhihu()


# 总结：直接传递参数简单，但是非要用什么闭包的形式传入参数，就觉得多此一举吧。