#!/usr/bin/python3

# 集合是一个无序不重复元素的集。基本功能包括关系测试和消除重复元素。
basket = {'apple', 'orange', 'apple', 'pear', 'orange', 'banana'}
print(basket)

# 以下演示两个集合的操作
a = set('abrcadabra')
b = set('alacazam')

print(a - b)
print(a | b)
print(a & b)
print(a ^ b)