'''
1、什么是for循环？
    重复做某件事情，for循环是python重复的第二种机制

2、为何要有for循环？
    理论上for循环能做的事情，while循环都可以做，之所以有for循环，一定是因为for循环在循环取值（遍历）上比while循环更简洁

3、如何用for循环
基本语法：
for 变量名 in 可迭代对象:  # 列表、字典、字符串、元组、集合
    代码1
    代码2
    代码3
'''

# 一、for循环的基本使用之循环取值
# 案例1：循环取值：
# 简单版
# l = [111, 222, 333, 444, 555, 666, 777]
# for x in l: # 取出一个值赋值给x，然后在执行代码块，然后在继续运行循环，直到列表的值取完为止
#     print(x)
# 复杂版

# 案例2：字典循环取值：
# dic = {'name' : 'yanzan', 'password' : "pwd123"}
# for i in dic:
#     print(i, dic[i])

# 案例3：字符串取值：
# msg = "my name is yankerp"
# for x in msg:
#     print(x)

# 二、总结for循环与while循环
'''
相同之处： 都是循环、for循环能干的事情，while循环都可以做到。
不同之处： while循环是条件循环，循环多少次取决于条件何时为假。
         但是for循环是取值循环或者说迭代循环，循环次数取决于in后面值的个数
'''

# 三、用for循环控制循环次数range()  顾头不顾尾
# for x in [1,2,3]:   # 有局限性
#     print("hello world")

# for x in range(3000):   # 循环3000次
#     print("hello world")

# username = "yanzan"
# password = '123'
#
# for x in range(3):
#     name = input("user name:")
#     pwd = input("user password:")
#
#     if name == username and pwd == password:
#         print("成功")
#         print("开始执行break直接退出本快循环体")
#         break
#     else:
#         print("失败")
# else:
#     print("for循环正常退出没有被break打断后输出结果！！！")

# 总结：for+break、for+else与while循环一模一样

# range 补充： for搭配range可以按照索引取值，但是很麻烦，所以不推荐使用
l = [111, 222, 333, 444, 555, 666, 777, 888, 9999, 0000]  # len() 查看有多少个
# for i in range(len(l)):
#     print(l[i])

# print(len(l))


# 四、for+continue for+continue和while+continue一模一样，退出本次循环立刻进入下次循环
# for i in range(6):
#     if i == 4:
#         continue
#     print(i)

# print('yanzan',end="")  # end 是换行符  使用给字符串\n 添加换行符


# 五、for循环的嵌套，外层循环执行一次，内层循环需要完整循环结束，外层继续循环一次，内层继续循环结束
# for x in range(2):
#     print("外层循环", x)
#     for i in range(3):
#         print("内层循环",i)
#         break
#     break

# 补充：终止for循环只有break一种方案





