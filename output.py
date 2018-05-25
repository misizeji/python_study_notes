#!/usr/bin/python3


for x in range(1, 11):
    print(repr(x).rjust(2), repr(x*x).rjust(3), end=' ')
    # 注意上一行的'end'用法
    print(repr(x*x*x).rjust(4))

# 两个print之间终端输出会有换行
print(1)
print(2)

for x in range(1, 11):
    print('{0:2d} {1:3d} {2:4d}'.format(x, x*x, x*x*x))