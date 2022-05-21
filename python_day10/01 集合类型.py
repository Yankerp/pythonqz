# 1、作用
# 1.1、关系运算

'''需求：提出来这两个列表当中共同的好友'''
friends1 = ['yanzan', 'zhangsan', 'lisi', 'wangwu']
friends2 = ['chengyao', 'laoliu', 'lisi', 'wangwu']

l = []
for x in friends1:
    if x in friends2:
        l.append(x)

'''通过集合来解决上面的需求'''

# 1.2、去重


# 2、定义
'''在{}内用逗号分隔开多个元素、多个元素需要满足以下三个条件  这个是前提，重点
    1、集合内元素必须为不可变类型
    2、集合内元素无序
    3、集合内元素没有重复
'''
# 3、类型转换
# print(set('hello'))   #  {'o', 'e', 'l', 'h'}
# print(set([111,222,33]))
# print(set({'name' : 'yanzan'}))


# 4、内置方法
friends1 = {'yanzan', 'zhangsan', 'lisi', 'wangwu'}
friends2 = {'chengyao', 'laoliu', 'lisi', 'wangwu'}

l = []
for x in friends1:
    if x in friends2:
        l.append(x)

# 4.1、取交集：两者共同的好友  & 符号
res = friends1 & friends2
print(res)

# 4.2、合集：取出两者所有的好友  并且去重
res2 = friends1 | friends2
print(res2)

# 4.3、取差集：取friends1独有的好友  &&  取friends2独有的好友
res3 = friends1 - friends2
res4 = friends2 - friends1
print(res3)
print(res4)

# 4.4、对称差集：求两个用户独有的好友们
print(friends1 ^ friends2)

# 4.5、父子集：包含的关系
s1 = {1, 2, 3}
s2 = {1, 2}
print(s1 > s2)  # s1 是 s2的爸爸, 或者说 s1 >= s2的时候 s1才是s2的爸爸

s1 = {1, 2, 3}
s2 = {1, 2, 3}  # s1 与 s2 互为父子

# ======================================集合去重======================================
# 二、集合的去重
'''局限性'''
# 1、只能针对不可变类型去重
# print(set([111,222,333,444,444,4444,44444,44444,]))

# 2、无法保证原来的顺序
l = ['yanzan', 'yanzan', 'zhangsan', 'lisi']
print(set(l))

# 集合后面的就是 循环、in不in、长度啥的不敲了
