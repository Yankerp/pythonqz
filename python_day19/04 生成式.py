# -*- coding utf-8 -*-

"""
@author:yankerp
@url:www.yankerphub.com
"""

# 列表生成式
# l = ['yanzan', 'zhangsan', 'lisi', 'wangwu']
# new_l = []
# for name in l:
#     if name.startswith('yan'):
#         new_l.append(name)
# print(new_l)

# new_l=[name for name in l if name.startswith('yan')]
# print(new_l)


# l1 = ['alex_dsb', 'lxx_dsb', 'wxxx_dsb', 'xqq_dsb']

# 案例实现：
# 用列表生成式把列表当中的元素都改为大写
# new_l = [name.upper() for name in l1]
# print(new_l)

# 用列表生成式把原列表当中的_dsb去除
# new_l2 = [name.strip('_dsb') for name in l1]
# print(new_l2)



# 二、字典生成式
# keys = ['name', 'age', 'info']
#
# info = {key:None for key in keys}
# print(info)


# 案例要求：把以下的列表数据添加到字典，但是不要gender
# items = [('name','egon'), ('age',18), ('gender','male')]
#
# new_dict = {key[0]:key[1]for key in items if 'gender' not in key}
# print(new_dict)


# 三、集合生成式 : 延瓒注意哦：集合内是不可变类型哦，元组、字符串、整形
info_list = (
    ('yanzan','yanzan1','yanzan2'),
    ('zhangsan','zhangsan1','zhangsan2'),
    ('lisi','lisi1','lisi2')
)
# jihe = {key for key in info_list}
# print(jihe,type(jihe))



# 四、元组生成式 !!!! 没有元组生成式，，这个是生成式表达式，得到的是生成器
# g=(i for i in range(10) if i > 3)
# print(g)  # <generator object <genexpr> at 0x7fdb0bd9d2e0>    ！！！！！！！没有元组生成式
#
# print(g.__next__())
# print(g.__next__())
# print(g.__next__())
# print(g.__next__())



# 案例需求：看看笔记里面有多少个字符


# 延瓒的第一次玩法
# l = []
# with open('本周内容', mode='rt', encoding='utf-8') as f:
#     while True:
#         try:
#             text = f.__next__()
#             res = len(text)
#             l.append(res)
#         except StopIteration:
#             break
#
#     print(l)
#     print(f"笔记当中的内容一共有{sum(l)}个字符")

# 思考了一下的第二次玩法
# with open('本周内容', mode='rt', encoding='utf-8') as f:
#     text_list = [len(text) for text in f.read()]
#     print("笔记内容一共有{txt}个字符".format(txt=sum(text_list)))

# 第三次牛逼的优化。效率最高
with open('本周内容', mode='rt', encoding='utf-8') as f:
    text_list = (len(text) for text in f.read())
    print(text_list)
    print("笔记内容一共有{txt}个字符".format(txt=sum(text_list)))



