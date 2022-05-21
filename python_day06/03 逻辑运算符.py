# 一、 and not or基本使用
# not：就是把紧跟其后的那个条件取反
# ps:not与紧跟其后的那个条件是一个不可分割的整体
# print(not 16 > 13)
# print(not True)
# print(not 10)
# print(not 0)
# print(not None)

# and：逻辑什么和什么，and用来链接左右两个条件，如果and两侧的条件都为真，最后才是真，两个条件同时为真，最终结果才为真
# print(True and 10 > 3 and 3 > 2 and 2 > 3)  # 链接多个条件的时候，条件都要为真，最后才为真


# or：逻辑或者， 用来链接左右两个条件，凡是有一个条件为真就为真,只有两个条件都为false的情况下，最终的结果就为false
# print(5 > 2 or 3 < 1)

# 二、优先级：
#     not>and>or
# 如果单独就只是一串and链接、或者说单独就是一串or链接，按照从左到右的顺序依次运算即可「偷懒原则」
# 如果是混用则需要考虑优先级

# print(3 > 4 and not 4 > 3 or 1 == 3 and 'x' == 'x' or 3 > 3)
print((3 > 4 and (not 4 > 3)) or (1 == 3 and 'x' == 'x') or 3 > 3)  # 优先级的算法

# not > and > or 优先级
