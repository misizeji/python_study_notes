#!/usr/bin/python3

age = int(input("please input dog's age:"))
#print("")
if age < 0:
    print("are you kidding me ?")
elif age == 1:
    print("equal age 14 years old")
elif age == 2:
    print("equal age 22 years old")
elif age > 2:
    human = 22 + (age - 2)*5
    print("equal human's age is: ", human)

# quit tips
input("click enter for exit!")