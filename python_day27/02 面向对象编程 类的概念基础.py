# -*- coding utf-8 -*-

"""
@author:yankerp
@url:www.yankerphub.com
"""


# 1、类体代码是在定义阶段就会立即运行，不是调用阶段

class Student:
    school = 'BeiJing清华'

    def out_put(student1):
        print(f"my name is {student1['name']}, my age is {student1['age']}, my welcome to {student1['school']}")


# 2、当Student类定义好之后，会立刻执行类体代码，产生名字，名字涉及到名称空间，因此得出，产生了属于Student类的名称空间
# 通过Student.__dict__方法可以看到名称空间中的名字，以字典的方式显示
# print(Student.__dict__)  # 'school': 'BeiJing清华', 'out_put':<function Student.out_put at 0x000001F044BBB7B8>

# 3、函数的调用一般就是先定义后引用，在引用的时候会在函数名后加一个括号， function()进行调用操作.
# 注意：类和函数不同的地方在于，类()不会调用类体代码的运行，因为类体代码是在定义阶段运行，So， 那么类()是产生一个对象。 这个很重要，这个是产生了一个对象，而不是执行代码~~~
"""
St1 = Student()  # 这个类加括号是产生了一个对象，一个空空如也的对象，对象当中什么都没有，还记得对象是什么吗？ 对象就是存放函数和数据的一个容器，那么此时产生的这个对象是一个空对象，意味着
# 产生的这个对象当中没有特定的数据和函数，但是！ 注意了，类主要是解决了对象的共有数据和功能，那么此时St1可以共用类当中的out_put函数功能以及school名称
# print(St1.__dict__)  # {} 此时这个对象就是个空空如也的对象，它目前有一个共享的库，Student里面有school方法和out_put方法
St1.__dict__['name'] = 'zhangsan'  # 为对象当中添加自己独有的数据
St1.__dict__['age'] = 20  # 为对象当中添加自己独有的数据
print(St1.__dict__)  # {'name': 'zhangsan', 'age': 20}


St2 = Student()  #  在产生一个对象，空空如也的对象
print(St2.__dict__) # 对象里面目前是空的，什么意思，也就是说，这个st2空空如也的对象和st1是完完全全分割开的，丝毫没有任何的关联，他们唯一有关联的就是共享的类的数据和功能，剩下的事情就各自添加
# 各自的一些独有的数据就好了
St2.__dict__['name'] = 'lili'
St2.__dict__['age'] = 16
print(St2.__dict__)   #  {'name': 'lili', 'age': 16}
"""


class Student:
    school = 'BeiJing清华'

    def out_put(student1):
        print(f"my name is {student1['name']}, my age is {student1['age']}, my welcome to {student1['school']}")


"""
# 无论是St1 = Student() 还是St2 = Student()只要类后面加括号就是在告诉python，Student类你好，我需要一个对象。 在大白话一点，你好类，我需要一个可以装数据和函数的一个箱子，但是我有点私心
# 我还想要你身体里面的数据和函数。 那么以上的st1得到的是一个空空的对象，但是st1可以使用类当中的数据和函数。

# st1 = Student()  # 你好类，我要一个对象，我还想要你身体里面的school和out_put函数
# print(st1.school) # 拿到了类身体里面的school数据
# print(st1.out_put) # 拿到了类身体里面的函数， So？ 当然st2也是一样的， 哪怕是st1000也一样如下：
# st2 = Student()
# print(st2.school)
# print(st2.out_put)
"""


# __init__方法：
class Student:
    school = 'BeiJing清华'

    def __init__(self):  # 当调用类的时候必须传入两个参数 name 和 age 和函数使用是一样的
        print(f"{self}调用了。。。。。。。。。。。")

    def out_put(self):
        print(f"my name is {self.name}, my age is {self.age}, my welcome to {self.school}, myaaa {self.sxxx}")


"""
到目前为止获得一个空空如也的对象，还需要自己向对象当中添加自己独有的数据，显得有些麻烦如下：
------------------------------------------------------------------------------------------------
St1 = Student()  # 这个类加括号是产生了一个对象，一个空空如也的对象，对象当中什么都没有，还记得对象是什么吗？ 对象就是存放函数和数据的一个容器，那么此时产生的这个对象是一个空对象，意味着
# 产生的这个对象当中没有特定的数据和函数，但是！ 注意了，类主要是解决了对象的共有数据和功能，那么此时St1可以共用类当中的out_put函数功能以及school名称
# print(St1.__dict__)  # {} 此时这个对象就是个空空如也的对象，它目前有一个共享的库，Student里面有school方法和out_put方法
St1.__dict__['name'] = 'zhangsan'  # 为对象当中添加自己独有的数据
St1.__dict__['age'] = 20  # 为对象当中添加自己独有的数据
print(St1.__dict__)  # {'name': 'zhangsan', 'age': 20}


St2 = Student()  #  在产生一个对象，空空如也的对象
print(St2.__dict__) # 对象里面目前是空的，什么意思，也就是说，这个st2空空如也的对象和st1是完完全全分割开的，丝毫没有任何的关联，他们唯一有关联的就是共享的类的数据和功能，剩下的事情就各自添加
# 各自的一些独有的数据就好了
St2.__dict__['name'] = 'lili'
St2.__dict__['age'] = 16
print(St2.__dict__)   #  {'name': 'lili', 'age': 16}


这就非常的麻烦，这意味着，如果我每次要一个对象，我需要在空空如也的对象当中添加自己独有的功能或者数据，我至少需要定义好多行，在类中init解决了自己定义的麻烦如下：
"""

# st1 = Student('zhangsan', 20)
"""
__init__就是初始化的意思，什么意思，可以理解为当调用类()这一瞬间，会直接调用init这个函数，然后产生对象. init可以理解为就是一个很普通的函数，下划线可以直接不用看它，也就是说，在这里定义了一个
init的函数，在类调用产生对象的时候会执行运行这个init的函数。 


st1 = Student('zhangsan', 20) 步骤分析：
1、当执行Student('zhangsan', 20) 过程的一刹那会调用init函数，发现init需要两个参数name和age，那么就把'zhangsan', 20传入到init函数当中，最牛逼的就是，init里面有三个参数self.name.age
那为什么写两个参数就可以呢？，是因为在调用类的时候，python会将对象直接传入self参数当中，self可以是任意的名字，这里可以写aaa，bbb等等，那再来分析一次：

2、当执行st1 = Student('zhangsan', 20)的时候会直接调用init函数，将对象名 st1，zhangsan，20这三个参数传给init函数，那么此时注意了。 init函数当中的self = st1, 那！！！在init体内代码
    def __init__(self, name, age):  # self = st1, name = "zhangsan", age = 20
        self.name = name  # st1.name = 'zhangsan'------------->st1.__dict__['name'] = 'zhangsan'
        self.age = age    # st1.age = 20 --------------------->st1.__dict__['age] = 20

那么此时，没有错，st1当中就存在了zhangsan 和 20这个独有的数据
"""
# st1 = Student('zhangsan', 20)  # 这个过程也被称为，实例化对象 专业术语就是叫实例化对象，说白了就是初始化生成一个对象
# st1.school = 'oldbey'  # st1.__dict__["school"] = oldbey
# print(st1.school)

# st2 = Student()


"""
类的函数功能和对象是一种绑定关系
"""


class Student:
    school = 'BeiJing清华'

    def __init__(self, name, age):  # 当调用类的时候必须传入两个参数 name 和 age 和函数使用是一样的
        # print(f"{self}调用了。。。。。。。。。。。")
        self.name = name
        self.age = age

    def out_put(self):
        print(f"my name is {self.name}, my age is {self.age}, my welcome to {self.school}")


s1 = Student('zhangsan',  20)
s2 = Student('lili',  16)


s1.out_put()  # Student.out_put(s1)
s2.out_put()  # Student.out_put(s2)







