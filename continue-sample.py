#!/usr/bin/python3

for letter in 'Runoob':
    if letter == 'b':
        continue
    print('now letter: ', letter)

var = 10
while var > 0:
    var = var - 1
    if var == 5:
        continue
    print('now var: ', var)

print("Good Bye", end="!!!!!")