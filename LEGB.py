#!/usr/bin/python3

x = int(2.9) # 内建作用域

g_count = 0 # 全局作用域
def outer():
    o_count = 1 # 闭包函数外的函数中
    def inner():
        i_count = 2 # 局部作用域


total = 0 # 这是一个全局变量
# 可写函数说明
def sum( arg1, arg2 ):
    total = arg1 + arg2 # total 在这里是局部变量
    print("sum total is: ", total)
    return total

#调用sum函数
sum( 10, 20 )
print("sum total is: ", total)