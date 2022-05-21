# # 基本运算符
# # 1、算数运算符
# print(10 + 3)
# print(10 - 3)
# print(10 * 3)
# print(10 / 3)
# print(10 // 3)  # 去除小数点只保留整数部分
# print(10 % 3)  # 取余数
# print(10 ** 3)  # 10的三次方
#
# # 2、比较运算符(> >= < <= ==, !=)
# print(10 > 3)
# print(10 == 10)
# print(10 >= 3)
# print(10 <= 3)
# name = input(">>>>")
# print(name != "yanzan")  # 判断是不是不等于
#
# # 3、赋值运算符
# """
# 变量的赋值：
#     = 等于号
# 增量赋值：
#     age = 18
#     age + 1
#     age = age = 19
#     增量赋值就是对上面的这个代码进行一个剪短的操作：
#     age = 18
#     age += 1  # 增量预算
#
#     age = 18
#     age *= 1 age -= 1 * // 都可以
# 链式赋值：
#     x = 10
#     y = x
#     z = y   这就是链接形式的一个赋值而已。
#     z = y = x = 10  剪短的写法
#
# 交叉赋值：
#     m = 10
#     n = 20
#     m指向20 n指向10
#     m,n = n,m
#
# # 解压赋值：
# """

# 解压赋值：
day = [111, 222, 333, 444, 555]
# day0 = day[0]
# day1 = day[1]
# day2 = day[2]
# day3 = day[3]
# day4 = day[4]
# print(day0, day1, day2, day3, day4)
#
# day0, day01, day02, day03, day04 = day
# day0, day01, day02, day03, day04, day05 = day
# day0, day01, day02, day03, = day

# 取前三个值
# day01, day02, day03, *_ = day
# print(day01,day02,day03)


# 取后三个值
*_, day01, day02, day03 = day
print(day01,day02,day03)

# 在这里的这个* 表示所有_ 表示了一个变量名，也就是说将所有的值赋予临时变量名_的意思，说白了就是列表的一种取值操作。



# day05 到这里正式结束

# 逻辑运算符


# 成员运算符
#
# 身份运算符
