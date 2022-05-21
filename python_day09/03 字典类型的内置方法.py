# 1、作用：字典是key对应值，和列表不一样的是字典具有描述信息
# 2、定义
"""
在{}内用逗号分隔开多个key和value，其中的value可以是任意的类型，但是key必须是不可变的类型
"""
d = {
    'name': "yanzan",
    111: "zhangsan",
    (222,): "lisi",
    2.1: "wangwu"
}
# d1 = {"name" : "yanzan"} # ----> d1 = dict(.....)

# print(d["name"])
# print(d[111])
# print(d[(222,)])
# print(d[2.1])

# 3、数据类型转换
info = [
    ['name', 'yanzan'],
    ('age', 18),
    ['aaa', 'email']
]

d = {}
for i in info:
    # print(i)
    d[i[0]] = i[1]
    # print(d)

res = dict(info)
# print(res)

info2 = [['name', "chengyao1"]]

c = {}
for x in info2:
    # print(x[0], x[1])
    # print(x)
    # c[x[0]] = x[1]
    # print(c)
    pass

d2 = {}
for k, v in info2:  # 这里的这个k和v等于列表的这个叫做解压复制
    # print(k, v)
    d2[k] = v
    # print(d2)

aaa, bbb, ccc, *_ = [1111, 2222, 333, 4444, 5555]  # 解压赋值
# print(aaa, bbb, ccc)

# 要求将列表当中的每个元素当中字典的key，value默认的值
list1 = ['name', 'age', 'ip', 'dizhi']

d3 = {}
for x in list1:
    pass
    # print(x)
    d3[x] = None
# print(d3)
d3 = {}.fromkeys(list1, None)  # 快速初始化一个字典和上面的代码是一样的效果，让所有的key都指向同一个value

d3['name'] = 'zhangsan'
# print(d3)

# 4、内置方法
# 优先掌握的操作
# 4.1、按key存取值：可存可取
d = {'k1': 111}
d['k1'] = 123123  # key如果存在则修改值
d['k2'] = 123321  # 如果key不存在的话会创建新的key和值
# print(d)  # {'k1': 123123, 'k2': 123321}

# 补充的内容例如下面案例：
d2 = {'name': 'zhangsan', 'name': 'lisi'}
print(d2['name'])  # 其中字典有两个name，那么输出的结果为最后添加的那个name，所以key为不可变类型并且不可以重复
# 4.2、长度len
print(len(d))  # len查看有多少个key,如果key重复的话当做一个

# 4.3、成员运算符 in和not in
print('k2' in d)
print('k1' in d)

# 4.4、删除
# 通用的删除方法：
# del(d['k1'])

# pop删除
# result = d.pop('k1') # pop 根据key删除
# print(result)  # pop的范围值是返回了删除的key对应value的值

# popitem删除
# res = d.popitem()  # 随机删除不传递任何的参数
# print(res)  # 返回一个元组，元组里面放的是删除的key和value

d3 = {'name': 'zhangsan', 'age': 18}
xin = {'name': 'lisi', 'master': '192.168.1.1'}

# keys、values、items
"""
目前的python解释器没有办法看到这个效果
info = {"name" : "yanzan"}
keys将字典当中的每一个key取出来类似于 >>>  ['name']
values将字典当中的每一个value取出来 >>> ['yanzan']
items将字典当中的key和value都取出来并以元组的形式存放 >>> [(name, yanzan)]
"""
n = {}
info = {"name" : "yanzan"}
info1 = [('name', 'yanzan')]
for x in info:
    print("这是元组当中第一个元素：{name}，第二个元素是{values}".format(name=x[0], values=x[1]))
    print(x)
aaa = ('name', 'yanzan')
a, b =aaa
print(f"这是元组的一个解压赋值：{a}   {b}")  # 验证了这一点

# 需要掌握的方法：

# print(d3.clear()) # 直接清空字典

""" 字典通过get取值，如果取值的key不存在的话最终会返回一个None
print(d3.get('111'))  # get 按照get取值，如果get通过key取值，这个key不存在的话会范围一个None
print(d3['1111'])
Traceback (most recent call last):
  File "/Users/ayao/PycharmProjects/pythonqz/python_day09/03 字典类型的内置方法.py", line 107, in <module>
    print(d3['1111'])
KeyError: '1111'
"""

""" update 内置方法更新字典
print(d3.update(xin))  # update就是更新字典，意思就是在原来字典的基础上更新新的内容，如果新的内容的key与原来字典的key冲突则不更新，只更新新的key
print(d3)
"""
d3 = {'name': 'zhangsan', 'age': 18}
# setdefault 这个意思就是说下面的这个aaa，123123 等同于== d3['aaa'] = 333 但是区别就是如果aaa这个key存在那就不会更改原来的key的值，如果不存在则添加
print(d3.setdefault('aaa', 123123))
print(d3.setdefault('name', '延瓒'))  # 这个字典里面已经存在name这个key了将不会进行更改，如果使用d3['name'] = '延瓒'的话原来的zhangsan就会被修改
result = d3.setdefault('name', 'zhangsan')  # 返回zhangsan 字典中key的对应值
print(result)
# setdefault 返回字典中key对应的值，setdefault是有返回值的


"""总结：
列表、元组、字典都为容器类型
列表字典可变类型、元组属于不可变类型
元组是一个不可变类型的列表，只能读不能写不能修改，如果列表当中有很多数据但是永远都不会改变的话可以存放到元组，因为元组占用的内存空间资源少。

学习到此，感觉基本数据类型的一些内置方法都是大同小异，都是要实现某些功能的。
"""
