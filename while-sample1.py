#!/usr/bin/python3

n = 100
sum = 0
counter = 1
while counter <= n:
    sum = sum + counter
    counter += 1
print("1 ~ %d sum is: %d" % (n,sum))