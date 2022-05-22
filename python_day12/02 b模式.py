# -*- coding utf-8 -*-

"""
@author:yankerp
@url:www.yankerphub.com
"""

"""
t:
    1、读写都是以字符串为单位的
    2、只能针对文本文件
    3、必须指定字符编码，即必须指定encoding参数
    
b:binary模式
    1、读写都是以bytes为单位，二进制，直接把硬盘的内容二进制读到内存，搬运工
    2、可以针对所有的文件
    3、一定不能指定字符编码encoding参数
    
总结：
1、在操作纯文本文件的时候t模式更加方便帮我们省去了编码解码的环节，b模式则需要手动进行编码解码
2、针对非文本文件，如图片视频音频等文件只能使用b模式，b模式也可以处理文本文件，说白了b模式可以处理任何文件，只是需要手动解码编码
"""

# with open('msk.png', mode='rb') as f:
#     res = f.read()
#
#
# with open('a.txt', mode='rb') as f:
#     res1 = f.read()
#     print(res1.decode())
#


"""扩展案例：之前的w模式的拷贝文件整改为通用的拷贝文件的代码，之前的"""
# with open(your_yfile, mode='rb') as f:
#     res = f.read() # 这里的问题就是read会一次性读到内存
#     with open(your_rfile, mode='wb') as f2:
#         f2.write(res)
#         print("文件拷贝成功，目标文件位于：{file}".format(file=res))
#
#
# with open(your_yfile, mode='rb') as f:
#     with open(your_rfile, mode='wb') as f2:
#         for line in f:
#             f2.write(line)
#     print("文件拷贝成功，目标文件位于：{file}".format(file=res))







