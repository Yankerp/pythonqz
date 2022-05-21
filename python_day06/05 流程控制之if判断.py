"""
语法1：
if  条件：
    代码1
    代码2
    代码3

"""
#
# age = 60
# is_beautiful = True
# star = '水瓶座'
#
# if 16 < age < 20 and is_beautiful and star == '水瓶座':
#     print("memme")


"""
语法2：
if  条件：
    代码1
    代码2
    代码3
else:
    代码1
    代码2
    代码3
"""

age = 60
is_beautiful = True
star = '水瓶座'

if 16 < age < 20 and is_beautiful and star == '水瓶座':
    print("在一起吧")
else:
    print("阿姨好，我逗你玩呢")

"""
语法3：
if  条件：
    代码1
    代码2
    代码3

elif 条件2：
    代码1
    代码2
    代码3

else:
    代码1
    代码2
    代码3
"""

# 以下为if语句的终极语法：
score = input("请您输入您的成绩：")
score = int(score)
if score >= 90:
    print("优秀")
elif score >= 80:
    print("lianghao")
elif score >= 70:
    print('普通')
else:
    print("垃圾")

# 到此python if流程控制 pythonday06的内容全部结束。
