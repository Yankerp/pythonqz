'''
基本数据类型：
    1、这个是什么？
        数据就是变量值，不同的数据类型的事物
    2、为什么要有它？
        因为变量值就是记录事物的，所以事物有很多类型，所以有不同的数据类型
    3、如何使用
'''

# 1、整数类型「整型」「浮点型」
# 1.1、整型int
'''整型就是一种阿拉伯数字呗，比如年龄、个数、身份证号等等和数字有关的
'''
age = 18
print(type(age))  # <class 'int'>

# 1.2、浮点型float
'''浮点型就是小数点的一些数字呗，比如12.11 22.11  2032.23等等，这个就是浮点类型
'''
xinzi = 12.9
print(type(xinzi))  # <class 'float'>

# 数字类型的其他作用
'''1、做一些数学运算(加减乘除) 2、做一些数字比较的场景
'''
# level = 1
# level += 1.1232
# level = level
# print(level)

'''做一些数字比较，比如年龄比较等等。
'''
# yanzan_age = 19
# chengyao_age = 10
# print(yanzan_age < chengyao_age)

# 2、字符串类型
# 2.1、str
# 字符串就是人类认识的一些东西，字符串通常的一些作用就是用来描述信息的状态，比如：你的名字叫啥，你住哪里？等等，一段话等等。
name = 'my name is yankerp'
print(type(name), name)  # my name is yankerp
x = '18'  # 由数字字符组成的字符串，是str而不是整数
# str定义的时候必须用引号括起来使用单引号，双引号，或者三个单引号都可以。用引号括起来的都是字符串

print('my name is ' + 'yanzan')  # 字符串之间是可以相加的，但是只能字符串与字符串相加，等于拼接。
print('name' * 10)  # 代表字符串的一个重复 十个name

# 3、列表类型（索引对应值 0 代表第一个）
# 3.1、list【按位置记录多个值通过index索引取值】
# 需求：延瓒有一个年龄，爱好，身高。以上的字符串、整数、浮点型都不能一次性存这些特定的数据，字符串可以存但是不好取，这个时候列表体现出来了。
# 定义：在中括号内，用逗号分割开，多个任意类型的值，一个值称为一个元素. 随意数据类型
yanzan = [19, '延瓒', 1.89, ['aaa', 'bbb']]
print(yanzan[2])  # 取值index 0 1 2 3 4 5 index 索引取值
# print(yanzan[3][1])

# 其他的用途：就是一些嵌套取值
students = [
    ['延瓒', 18, 1.78],
    ['诚邀', 19, 1.66]
]
print(students[1][1])

# 4、字典类型「dict」key = value
# 现在的需求就是把延瓒的年龄、性别、身高、爱好存下来例如：
aaa = ['yanzan', 18, 1.90, '爱学习']  # 列表可以实现这个功能，但是需要事先记住index的值是什么在来取值，比如有100个人，这样的话需要记住index的0 1 2 3是什么来取
# 列表没有描述性的功能，列表反映的是顺序，位置，和index对应的值需要记录

# 字典的话key通常是字符串类型，用来存多个值，每个值都有对应的key，在{}内用逗号分割开，其中key通常是字符串类型(字典是没有顺序的) 但是列表是有序的。
info = {
    'name': '延瓒',
    'age': 18,
    'aihao': '学习'
}
print(info['name'])

# 列表的嵌套取值

info = [
    {
        'name': '延凯',
        'age': 19,
        'url': 'beijing'
    },
    {
        'name': '延瓒',
        'age': 19,
        'url': '杭州'
    },
    {
        'name': '延冰火',
        'age': 19,
        'url': '苏州'
    },
    {
        'name': '言语量',
        'age': 19,
        'url': '山西'
    },
    {
        'name': '延凯',
        'age': 19,
        'url': 'beijing'
    }
]

print(info[1]['name'], info[1]['age'], info[1]['url'])

# 5、布尔值bool「记真和假的」 说白了，就是一种状态，0和1 也行，ok和no也行，这就是一种表达状态，叫做bool值
isOK = True
isno = False

print(isOK)

# 到此p67-day04-17 学习结束 待总结
print(aaa)

name2 = {
    "info1": {"name": "yanzan", "password": "pwd123.coms"},
    "info2": {"name": "zhangsan", "password": "ywyankeerp"}
}
print(name2['info1']['password'])

name3 = [
    {"name": "zhangsan", "url": "beijing"},
    {"name": "lisi", "url": "shanghai"},
    {"name": "wangwu", "url": "shenzheng"}
]
print(name3[1]['name'])
