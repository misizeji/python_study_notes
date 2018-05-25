#!/usr/bin/python3

tel = { 'jack': 4098, 'sape': 4139}

tel['guido'] = 4127
print(tel)

print(tel['jack'])

del tel['sape']

tel['irv'] = 4127
print(tel)

print(list(tel.keys()))

# 排序
print(sorted(tel.keys()))

print(dict([('sape', 4139),('guido', 4127),('jack', 4098)]))

print(dict(sape=4139, gudio=4127, jack=4098))

# 遍历
knights = {'gallahad': 'the pure', 'robin': 'the brave'}
for k,v in knights.items():
    print(k, v)