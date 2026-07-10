import time

My_time = int(input("enter your time in seconds: "))

for x in reversed(range(0,My_time)):
    second = x % 60
    minutes = int(x/60)%60
    hour = int(x/3600)
    print(f"{hour:02}:{minutes:02}:{second:02}")
    time.sleep(1)

print("times up ")
