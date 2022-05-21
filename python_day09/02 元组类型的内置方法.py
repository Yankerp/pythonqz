"""
元组就是一个不可变的列表，元组只用来读的操作，不能改。
"""
# 1、作用：按照索引位置存放多个值，只用于读，不用于改
# 2、定义
t = (111, 222, 333, 'yanzan')  # ---> t = tuple(111,222,333,'yanzan') 元组当中可以存放多个任意的数据类型，和列表是一样的tuple元组类型
# print(type(t), t)
# t[0] = 1111111 # 元组是不可以改变的。所以会直接报错

# 例如以下：
t1 = (111, 222, 333, ['yanzan', 'zhangsan'])
t1[3][1] = 'lisi' # 这个是可以改的
x = (1)  # 注意：如果是单独的一个括号的话，就不是元组， 如果元组当中只有一个元素，必须加个，分隔开。 有，号的元组才是真正的元组


# 3、类型转换「和列表一样能被for循环循环的数据类型都可以转换为元组」
l = [111,222,333]
l1 = tuple(l)  # 将列表转换为字典
# print(l1)

name = 'yanzan'
name2 = tuple(name)  # 将name的 yanzan拆分开存入到元组('y', 'a', 'n', 'z', 'a', 'n')
# print(name2)


# 4、内置方法
# 4.1、按索引取值「正向取、反向取」
tt = (111,222,333,'zhangsan')
print(tt[0])
print(tt[:-1])
print(tt[-1])

# 4.2、切片
print(tt[0:3:2])

# 4.3、长度
print(len(tt))

# 4.4、成员运算 in 和not in
print(111 in tt)

# 4.5、循环
for i in tt:
    # print(i)
    pass

# 内置方法：index, count   元组就两个内置方法
print(tt.index(111))  # 看以下111的index索引值
print(tt.count('zhangsan'))  # 查看有几个zhangsan



















