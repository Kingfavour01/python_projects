import time
import datetime
date = datetime.date.today()
times = datetime.datetime.now()
times = times.strftime("%H:%M:%S %d %m %Y")
start_time = time.perf_counter()

target_datetime = datetime.datetime(2030, 1, 2, 12, 39, 33)
current_date = datetime.datetime.now()

if target_datetime < current_date:
    print("target date has passed")
else:
    print("target date has not passed")
for i in range(10000000):
    pass
end_time = time.perf_counter()

elapsed_time = end_time - start_time
print(date)
print(times)
print(f"Elapsed time: {elapsed_time:.1f}seconds")


