# 什么是条件？什么可以当作条件？为何要用条件？

# 条件可以是比较运算符
age = 10
print(age > 11)  # 条件判断之后返回true、false。会得到一个bool值

# 条件也可以直接用bool值 false true
is_beatiful = True
print(is_beatiful)

# 上面的这两种都是显示的bool值，但是还有第二大类，就是不显示的bool值，就是所有的值都可以当作条件去用
# 其中0、None、空为假 其他的类型都为真