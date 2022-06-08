# -*- coding utf-8 -*-

"""
@author:yankerp
@url:www.yankerphub.com
"""

# os模块是与操作系统交互的一个接口
import os

# print(os.getcwd()) # 获取当前工作目录，即当前python脚本工作的目录路径,根据平台，可以自动设置/ 或者 \
# os.chdir(r"E:\pythonqz\python_day21")  # 改变当前脚本工作目录；相当于shell下cd
# os.curdir  # 返回当前目录: ('.')       未解
# os.pardir  # 获取当前目录的父目录字符串名：('..')    未解
# os.makedirs("/usr/local/src/aaa/bbb/ccc/ddd/eee") # 相当于linux的 mkdir -p 创建目录
# os.removedirs("/usr/local/src/aaa/bbb/ccc/ddd/eee") # 若目录为空，则删除，并递归到上一级目录，如若也为空，则删除，依此类推
# os.mkdir("目录") # 生成单级目录；相当于shell中mkdir dirname
# os.rmdir("目录") # 删除目录，如果目录不为空的话，就报错了
# os.listdir('dirname') # 列出指定目录下的所有文件和子目录，包括隐藏文件，并以列表方式打印
# os.remove('filename') / os.remove('dirname/filename')  # 删除一个文件
# os.rename("yankerp", "zhangsanyankerp")  # 重命名文件/目录
# os.stat('path/filename') # 获取文件/目录信息 这个牛逼
# os.sep # 输出操作系统特定的路径分隔符，win下为"\\",Linux下为"/"
# os.linesep    # 输出当前平台使用的行终止符，win下为"\t\n",Linux下为"\n"
# os.pathsep    # 输出用于分割文件路径的字符串 win下为;,Linux下为:
# os.name    # 输出字符串指示当前使用平台。win->'nt'; Linux->'posix'
# os.system("df -h, bashshell命令")  # 运行shell命令，直接显示
# os.environ #  获取系统环境变量
# os.path.abspath(path)  # 返回path规范化的绝对路径
# os.path.split(path)  # 将path分割成目录和文件名二元组返回
# os.path.dirname(path) # 返回path的目录。其实就是os.path.split(path)的第一个元素
# os.path.basename(path)  # 返回path最后的文件名。
# os.path.exists(path) dirname/filename  #  如果path存在，返回True；如果path不存在，返回False
# os.path.isabs(path)  # 如果path是绝对路径，返回True
# os.path.isfile(path)  # 如果path是一个存在的文件，返回True。否则返回False
# os.path.isdir(path)  # 如果path是一个存在的目录，则返回True。否则返回False
# os.path.join(path1[, path2[, ...]]) # 拼接
# os.path.getatime(path)  返回path所指向的文件或者目录的最后存取时间
# os.path.getmtime(path)  返回path所指向的文件或者目录的最后修改时间
# os.path.getsize(path) 返回path的大小 目录/文件


# 作业:统计一个文件夹中所有文件的一些大小


