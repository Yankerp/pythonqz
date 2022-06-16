# -*- coding utf-8 -*-

"""
@author:yankerp
@url:www.yankerphub.com
"""
import os


def file_size_count(your_dir_path):
    if os.path.isdir(your_dir_path):  # 判断输入的是否是一个目录
        file_dir_name = os.listdir(your_dir_path)

        for files in file_dir_name:
            file_result = os.path.join(your_dir_path, files)
            file_size_count(file_result)

    elif os.path.isfile(your_dir_path):
        file_bytes = os.path.getsize(your_dir_path)
        with open('file_size.txt', mode='at', encoding='utf-8') as f:
            f.write("此文件：{file} 大小为：{size} Bytes\n".format(file=your_dir_path, size=file_bytes))

    else:
        print("不是一个目录也不是一个文件")
        return 'error'


file_size_count('/Users/ayao/PycharmProjects/pythonqz')