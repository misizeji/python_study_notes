#!/usr/bin/python3


print('{0} and {1}'.format('Google', 'Baidu'))
print('{1} and {0}'.format('Google', 'Baidu'))

print('站点列表 {0}, {1}, 和 {other}'.format('Google', 'Baidu', other = 'Taobao'))

import math

print('常量PI的值近似为：{}'.format(math.pi))
print('常量PI的值近似为：{!r}'.format(math.pi))
print('常量PI的值近似为：{0:.3f}'.format(math.pi))

table = {'Google':1, 'Runoob':2, 'Taobao':3}
for name, number in table.items():
    print('{0:10} ===> {1:10d}'.format(name, number))

# 如果你有一个很长的格式化字符串, 而你不想将它们分开, 那么在格式化时通过变量名而非位置会是很好的事情。最简单的就是传入一个字典, 然后使用方括号 '[]' 来访问键值 :
print('A: {0[Runoob]:d}; B: {0[Google]:d}; C: {0[Taobao]:d}'.format(table))
# 也可以通过在 table 变量前使用 '**' 来实现相同的功能：
print('A: {Runoob:d}; B: {Google:d}; C: {Taobao:d}'.format(**table))

print('常量PI的值近似为：%5.3f' % math.pi)
