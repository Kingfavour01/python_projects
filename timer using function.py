import time
def count(start=0 ,end=0):
    for x in range(start,end+1):
        print(x)
        time.sleep(1)
    print("done")


user_start = int(input("enter your start time: "))
user_stop = int(input("enter your start time: "))

count(user_start,user_stop)


