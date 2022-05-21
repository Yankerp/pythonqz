# 如何接受用户的输入
# username = input("请您输入您的账号：")
# print(username, type(username))  # 在这里input传入的东西都是字符串的类型

# age = input("请您输入您的年龄：")
# age = int(age)
# print(age, type(age))
# print(age > 18)


# 2、格式化输出
## 2.1、%的方式
info = "my name is %(name)s, my age is %(age)s" % {"name": 'yanzan', "age": '19'}
info2 = "my name is %s, my age is %s" % ('yanzan', '18')
print(info, info2)

## 2.1、format

# 按照位置
'my name is {}'.format(12)

# 按照位置
'my name is {}, my age is {}'.format('yanzan', 19)
# 按照位置index取值方式
'my name is {0}{0}{0}, my age is {1}'.format('zhangsan', 19)

# 打破位置的限制，按照key=value取值
res = 'my name is {name}, my age is {age}'.format(name="yanzan", age=19)
res2 = '我的名字是{name}， 我的年龄为：{age}'.format(age=19, name="yanzan")
print(res)
print(res2)

name = "yanzan"
pwd = 123
print("my name is {name}, my password:{pwd}".format(name=name, pwd=pwd))

# 按照f""格式化输出
name = "yanzan"
print(f'my name is {name}')
