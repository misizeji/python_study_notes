#!/bin/usr/python3

sites = ["Baidu", "Google", "Runoob", "Taobao"]
for site in sites:
    if site == "Runoob":
        print("NewBird lesson!")
        break
    print("cycle data " + site)
else:
    print("no cycle data!")
print("finish cycle data!")