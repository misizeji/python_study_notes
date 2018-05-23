#!/usr/bin/python3

list = [1, 2, 3, 4]
it = iter(list)
print(next(it))
print(next(it))
print(next(it))
print(next(it))

print("")

# new method for call
it = iter(list)
for x in it:
    print(x, end = " ")