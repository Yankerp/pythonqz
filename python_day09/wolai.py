n = {}
info = {"name" : "yanzan"}
info1 = [('name', 'yanzan')]
for x in info1:
    print("这是元组当中第一个元素：{name}，第二个元素是{values}".format(name=x[0], values=x[1]))
    print(x)
aaa = ('name', 'yanzan')
a, b =aaa
print(f"这是元组的一个解压赋值：{a}   {b}")  # 验证了这一点