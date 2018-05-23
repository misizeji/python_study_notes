#!/usr/bin/python3

a = ["Google", "Baidu", "Runoob", "Taobao", "QQ"]
for i in range(len(a)):
    print(i, a[i])

for letter in 'Runoob':
    if letter == 'b':
        break
    print('now letter: ', letter)

var = 10
while var > 0:
    print('now var: ', var)
    var = var - 1
    if var == 5:
        break

print("Good Bye", end="!!!!!")