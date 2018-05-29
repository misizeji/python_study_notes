#!/usr/bin/python3


class People():
    name = ''
    age = 0
    __weight = 0

    def __init__(self, n, a, w):
        self.name = n
        self.age = a
        self.__weight = w

    def speak(self):
        print("%s says that I am %d years old"%(self.name, self.age))


class Student(People):
    grade = 0

    def __init__(self, n, a, w, g):
        People.__init__(self, n, a, w)
        self.grade = g

    def speak(self):
        print("%s says that I am %d years old, I am in grade %d"%(self.name, self.age, self.grade))


class Speaker():
    topic = ''
    name = ''

    def __init__(self, n, t):
        self.name = n
        self.topic = t

    def speak(self):
        print("I am %s, a speech speaker, my topic is %s"%(self.name, self.topic))


class Sample(Speaker, Student):
    a = ''

    def __init__(self, n, a, w, g, t):
        Student.__init__(self, n, a, w, g)
        Speaker.__init__(self, n, t)

test = Sample("Tim", 25, 80, 9, "python")
# 方法同名，方法调用括号内，父类排列从左至右依次查找speak()方法，所以此处的speak()方法为speaker类里面的speak方法
test.speak()