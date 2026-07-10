import random
rnd1 = random.randint(0,10)
rnd2 = random.randint(0 , 11)

num = int(input("enter a number:"))



for num in range(1, 101):
    if num % 3 == 0 and num % 5 == 0:
        print("FizzBuzz")
    elif num % 3 == 0:
        print("Fizz")
    elif num % 5 == 0:
        print("Buzz")
    else:
        print(num)