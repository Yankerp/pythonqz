# -*- coding utf-8 -*-

"""
@author:yankerp
@url:www.yankerphub.com
"""

# import json
#
# nameinfo = {
#     'name' : 'zhangsan',
#     'age' : 19,
#     'is' : True
# }
#
# with open('aaa.json', mode='wt', encoding='utf-8') as f:
#     (f.write(json.dumps(nameinfo)))
#
# with open('aaa.json', mode='rt', encoding='utf-8') as f:
#     res = f.read()
#     print(json.loads(res), type(json.loads(res)))
#
# with open('aaa.json', mode='rt', encoding='utf-8') as f:
#     print(json.load(f))




import pickle

nameinfo = {
    'name' : 'zhangsan',
    'age' : 19,
    'is' : True
}

with open('aaa.txt', mode='wb') as f:
    f.write(pickle.dumps(nameinfo))


with open('aaa.pkl', mode='rb') as f:
    print(pickle.load(f))




