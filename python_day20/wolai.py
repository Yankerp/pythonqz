# -*- coding utf-8 -*-

"""
@author:yankerp
@url:www.yankerphub.com
"""

# nums = [-3, 4, 7, 10, 13, 21, 43, 77, 89]

# 方式1：整体的遍历
# 比如说查找的数字是7

# for n in nums:
#     if n == 7:
#         print("找到了")


# nums = [-3, 4, 7, 10, 13, 21, 43, 77, 89]
#
# def erfenfa(num, new_list):
#     zhongjian = len(new_list) // 2  # 取到中间的这个数字
#     print(new_list)
#     if len(new_list) == 0:
#         print("输入非法,没有找到.....")
#     elif num > nums[zhongjian]:
#         new_you = new_list[zhongjian + 1:]
#         erfenfa(num, new_you)
#
#     elif num < nums[zhongjian]:
#         new_zuo = new_list[:zhongjian]
#         erfenfa(num, new_zuo)
#
#     else:
#         print("找到了")


# erfenfa(-3, nums)


import module_yanzan

module_yanzan.func()


def func():
    print("这是wolai的代码")


func()
