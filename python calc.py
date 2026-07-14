
numb1 = float(input("input your first number: "))
operator = input("enter your operator ( +, - , / , *) : ")
numb2 = float(input("input your second number: "))

if operator == "+":
    result =(numb1 + numb2)
    print(result)
elif operator == "-":
    result =(numb1 - numb2)
    print(result)
elif operator =="/":
    result = (round(numb1/numb2 , 3))
    print(result)
elif operator == "*":
    result = (numb1 * numb2)
    print(result)

else:
    print(f"{operator} this is not an operator")