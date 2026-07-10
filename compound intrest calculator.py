principal = 0
rate = 0
time = 0

while principal <= 0:
    principal = float(input("input your principal amount: "))
    if principal <=0:
     print("principal cant be less than or equal to zero")
while rate <= 0:
    rate = float(input("input your rate of interest: "))
    if rate <=0:
     print("rate cant be less than or equal to zero")
while time <= 0:
    time = float(input("input your Time(years): "))
    if rate <=0:
     print("time cant be less than or equal to zero")

total = principal * pow((1 + rate / 100) ,  time )

print(f"Your total interest in {time :.2f}years if your principal was ${principal:,.2f} at a rate of {rate:.2f}% is = ${total:,.2f}")
