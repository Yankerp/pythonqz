# 1、作用：存多个值，并且是index索引对应值，按位置存放多个值

# 2、定义
l = [111,222,333] #  l = list([111,222,333])

# 3、类型转换:但凡能够被for循环遍历的类型都可以当做参数传给list转换为列表
# 实际上list的底层工作原理等于调用了一个for循环，
# 3.1、字符串
res = list("my name is yanzan")
l = []
for x in "my name is yanzan":
    l.append(x)

# 3.2、字典：
res2 = list({'name' : "yanzan", 'password' : "pwd123.com"})
# print(type(res2), res2)

# 4、内置方法
# 优先掌握的操作：
# 1、按照索引取值（正向存取+反向存取）:即可取也可以改
l = [111,222,333,'yanzan']
# 正向取
# print(l[0])
# 反向取
# print(l[-1])
# 可存可改
l[0] = 22222  # index索引存在则修改对应的值
# print(l)
# 索引不存在则直接报错，indexerror不存在这个索引（无论是取还是改，都会报错）
# l[4] = "dawdaw"
# print(l)

# 2、切片（顾头不顾尾，步长） 切片就是拷贝行为，相当于浅拷贝
l = [111,222,333,'yanzan',1212,33333121221,'lisi']
# print(l[0:3])
# print(l[0:5:2])  # 步长和字符串一个样子
# 反向切片
# print(l[:2])

# 3、长度
# print(len(l)) # 统计列表元素的个数


# 4、成员运算in和not in
# print(111 in l)


# 5、追加
l.append(3333333333)
l.append(44444444444)

# 6、插入值[(self, __index: SupportsIndex, __object: _T) ->]
l1 = [111,222,333]
l1.insert(0, 'dingding')  # 在0号索引直接插入值，append只能在末尾追加值
# print(l1)
# 案例1：
new_l = [1,2,3]
l = [111,'zhangsan']
# for x in new_l:
#     l.append(x)
# print(l)

# 列表extend实现上述代码案例1
l.extend(new_l)
# print(l)


# 7、删除
l = [111,'zhangsan',222,333,44444,555555]
# 方式一：通用的删除方法，没有返回值，只是单纯的删除
# del l[0]
# x = del l[0] 不支持复制语法，抛出异常
# print(l)
# 方式二：list.pop----->pop(self, __index: SupportsIndex = ...)
# l.pop() # pop根据索引删除，如果这里pop不指定索引默认删除的是最后一个
# l.pop(1)  # 删除zhangsan index为1
# x = l.pop(1)  # 删除之后会有返回信息，比如删除了zhangsan就会返回zhangsan这个值，这就是和del的区别
# print(x)

# 方式三：list.remove
# l.remove('zhangsan')  # 按照index元素的信息,根据元素删除,remove返回None没有返回值
# res = l.remove('zhangsan')    # 如果元素不会会直接报错
# print(res)

# 8、循环
# for x in l:
#     print(x)


# 二、需要掌握的操作
# l = [1, 'aaa', 'bbb','aaa','aaa','cccc']
# print(l.count('aaa'))  # aaa出现的次数
# print(l.index('aaa'))  # 返回第一个找到的index索引，找不到报错
# print(l.clear())  # 清空全部的列表
# print(l.reverse()) # 把列表倒过来
# print(l) # ['cccc', 'aaa', 'aaa', 'bbb', 'aaa', 1]

# l1 = [11,32,11,65,0,1.1,0.1]
# print(info.sort(reverse=False))  # reverse反转的意思/ True false升序，降序
# print(l1)

# sort:sort比较运算当中只能针对列表内元素全都是相同数据类型的数据排序字符串也可以比大小

"""
字符串是可以比大小的，多数都是数字的，但是字符串可以比大小，abcdefg 按照ASCI码表的顺序区分字符的大小
"""