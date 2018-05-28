#!/usr/bin/python3


""" 关键词 with 语句就可以保证诸如文件之类的对象在使用完之后一定会正确的执行他的清理方法 """

try:
    with open("myfile.txt") as f:
        for line in f:
            print(line, end="")
except FileNotFoundError:
    print("file not found! ")
finally:
    print("execute finish")