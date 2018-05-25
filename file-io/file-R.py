#!/usr/bin/python3


# read file
f = open("foo.txt", "r")

r_str = f.read()
print(r_str)

f.close()

# read line
f = open("foo.txt", "r")

r_str = f.readline()
print(r_str)

f.close()

# read lines
f = open("foo.txt", "r")

r_str = f.readlines()
for x in range(len(r_str)):
    print(r_str[x])

f.close()

