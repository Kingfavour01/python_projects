principal = 0
rate = 0
time = 0

while True:
    principal = float(input("input your principal amount: "))
    if principal <0:
     print("principal cant be less than or equal to zero")
    else:
        break
while True:
    rate = float(input("input your rate of interest: "))
    if rate <0:
     print("rate cant be less than or equal to zero")
    else:
        break
while True:
    time = float(input("input your Time(years): "))
    if rate <0:
     print("time cant be less than or equal to zero")
    else:
        break

total = principal * pow((1 + rate / 100) ,  time )

print(f"Your total interest in {time :.2f}years if your principal was ${principal:,.2f} at a rate of {rate:.2f}% is = ${total:,.2f}")
