# 1、作用

# 2、定义
# msg = "hello"  # msg = str(hello)

# 3、类型转换
'''
str 可以把其他任意类型都可以转为字符串
'''
print(str({'name': "yanzan"}))
print(type(str({'name': "yanzan"})))

# 4、使用(内置方法：)
'''
优先掌握
需要掌握
了解
'''
# 4.1、优先掌握
# 4.1.1、按索引取值（正向取、反向取）
msg = "hello world"
# 正向取：
print(msg[0])
# 反向取：
print(msg[-1])
# 不能改：
# msg[0] = "H"  # 这个和列表是不一样的，不能直接改。 字符串类型是一个不可变类型，它是一个整体

# 4.1.2、切片【顾头不顾尾】 索引的扩展应用. 从一个大字符串当中复制出来一个子字符串
print(msg[0:5])  # hello
# 步长
print(msg[0:5:2])  # 步长为2 0-5   hlo
# 反向步长（了解）
print(msg[0:5:-1])
print(msg[5:0:-1])  # 反着来

# 4.1.3、len 统计字符的个数
print(len(msg))

# 4.1.4、成员运算in 和not
name = "yanzan is ok"
print('yan' in name)  # True
print('yan' not in name)

# 4.1.5、移除空白strip
msgs = "     yanzan       "
print(msgs.strip())  # strip 默认移除字符串左右两侧的空格
msgs = "*********yanzan********"
print(msgs.strip('*'))
# strip 只会去除两边的，不会去除中间的部分

msges = "******/////===== yanzan *****/////---====="
print(msges.strip('*-/= '))  # 牛逼！！！

# 应用：
# pwd = '123'
# password = input("请您输入密码").strip()
# if password == pwd:
#     print('成功')
# else:
#     print("错误")

# 4.1.6、切分split：把一个字符串按照某种分隔符进行切分，得到一个列表
info = "yanzan:zhangsan:lisi:wangwu:chengyao"
# print(info.split(':'))  # 对于特定规律的字符串通过split来分割，默认是空格分割，传入:意思就是按照:进行分割，分割成列表类型：
# ['yanzan', 'zhangsan', 'lisi', 'wangwu', 'chengyao']

# 4.1.7、循环
# for x in info:
#     print(x)


# 4.2、需要掌握的操作
# 4.2.1、strip、lstrip、rstrip
aaa = "******yanzan********"
print(aaa.strip('*'))  # 左右两边去除
print(aaa.lstrip('*')) # 去除左边
print(aaa.rstrip('*')) # 去除右边

# 4.2.2、lower、upper
print(aaa.lower())  # 变成小写
print(aaa.upper())  # 变成大写

# 4.2.3、startswith、endswith
aaa2 = "yanzan is ok"
print(aaa2.startswith('yanzan'))  # 以什么开头
print(aaa2.endswith('ok'))  # 以什么结尾

# 4.2.4、split、rsplit
info2 = "yanzan:zhangsan:lisi"
print(info2.split(':',1))   # 切割
print(info2.rsplit(':',1))

# 4.2.5、join：将列表拼接成字符串
info_name = ['yanzan','zhangsan','lisi']
print("".join(info_name))   # 将列表元素按照某个分隔符，把列表内的字符串类型拼接成大的字符串 例如：[111,222,'zhangsan'] 就不可以了

# 4.2.6、replace
msgs1 = 'my name is yanzan'
print(msgs1.replace('my',"MY",1))  # 后面的那个1就是只改一个

# 4.2.7、isdigit 判断字符串是否由数字组成. 如果是那就为True
msgs2 = '8271389dawjlda71297219'
msgs3 = '827138971297219'
print(msgs2.isdigit())
print(msgs3.isdigit())



