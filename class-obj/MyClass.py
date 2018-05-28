#!/usr/bin/python3


class MyClass:
    """ a simple class define """
    i = 12345
    def f(self):
        return "Hello world"


# 实例化
x = MyClass()

# for members and method
print("MyClass 类属性i为： ", x.i)
print("MyClass 类方法f输出为： ",x.f())
