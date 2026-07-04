item = str( input(f" input the name of item: "))
price = float (input(f" input the price of the item : "))
amount = int( input ( f" input the quantity of items bought: "))

total_price = price * amount

print (f" your shopping cart contains {item}/s at ${price} in this {amount} units .")
print(f" your total price is : { round(total_price , 2)}" )
print(f" Have a blessed day ❤️❤️.")
