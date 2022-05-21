# 1、成员运算符：
print('ya' in 'this is a yanzan')  # 判断一个子字符串是否存在与一个大字符串当中
print(111 in [111,222,333,444])   # 判断元素是否在列表
print('name' in {'name':'yanzan', 'password': 'pwd123'})   # 判断字典的key是不是在里面

# not in
print('name' not in {'name':'yanzan', 'password': 'pwd123'})  # name不在这个里面吗？ 在为false 不在为true

# 2、身份运算符：

# is：判断两个值的id是否相等
a = 111
b = a
print(a is b)