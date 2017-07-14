import random

guessNumber = random.randint(0, 10)
while True:
    temp = input("please input a number between 0 ~ 20:")
    inputNumber = int(temp)
    if guessNumber < inputNumber:
        print("your input number is bigger")
    elif guessNumber > inputNumber:
        print("your input number is smaller")
    elif guessNumber == inputNumber:
        print("wow, you are a lucky dog!")
        break
