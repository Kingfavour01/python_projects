row = int(input("input the amount of rows for your rectangle : "))
col = int(input("input the amount of colon for your rectangle : "))
symbol = str(input("pick any symbol: "))

for y in range(row):
    for x in range(col):
        print(symbol, end="")
    print(y)