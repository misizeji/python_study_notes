#!/usr/bin/python3


class people:
    name = ''
    age = 0
    __weight = 0
    def __init__(self, n, a, w):
        self.name = n
        self.age = a
        self.__weight = w

    def speak(self):
        print(" %s say that I am %d years old" %(self.name, self.age))

class student(people):
    grade = ''
    def __init__(self, n, a, w, g):
        # 调用父类的构造函数
        people.__init__(self, n, a, w)
        self.grade = g
    # 覆盖父类中的speak方法
    def speak(self):
        print("%s say that I am %d years old I study in grade %d"%(self.name, self.age, self.grade))

s = student('Bob', 10, 45, 3)
s.speak()