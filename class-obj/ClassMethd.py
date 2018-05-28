#!/usr/bin/python3


# 类定义
class people:
    # 定义基本属性
    name = ''
    age = 0
    # 定义私有属性，私有属性在类外部无法直接访问
    __weight = 0
    # 定制构造方法
    def __init__(self, n, a, w):
        self.name = n
        self.age = a
        self.__weight = w

    def speak(self):
        print("%s say I am %d years old" %(self.name, self.age))


p = people('Runoob', 10, 30)
p.speak()

