# -*- coding utf-8 -*-

"""
@author:yankerp
@url:www.yankerphub.com
"""

# 算法：是高效解决问题的办法：
# 算法之二分法：

# 需求：有一个按照从小到大顺序排列的数字列表
#   需要从该数字列表中找到我们想要的那个数字
#   如何做更加高效？？？？


# nums = [-3, 4, 7, 10, 13, 21, 43, 77, 89]
#
# find_num = 13
# nums[]

# 方案一：整体遍历，效率太低
# for num in nums:
#     if find_num == num:
#         print('find it')
#         break

# 方案二：二分法
nums = [-3, 4, 7, 10, 13, 21, 43, 77, 89]


def binary(find_num, you_list):
    if len(you_list) == 0:
        print('不存在这个值')
        return
    count = len(you_list) // 2  # 得到列表中间的值,index值
    if find_num > you_list[count]:
        new_list = you_list[count + 1:]
        binary(find_num, new_list)
    elif find_num < you_list[count]:
        new_list = you_list[:count]  # 得到新的列表左边的值
        binary(find_num, new_list)

    else:
        print("找到了.......")


binary(1, nums)  # 二分算法实现。
