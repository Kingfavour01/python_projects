from string.templatelib import convert

foods = []
prices = []
total = 0

while True:
    food = str(input("enter your list of food(press q to quite): "))
    if food.lower() == "q":
        break
    else:
        price = float(input("enter the price of food items:$ "))
        foods.append(food)
        prices.append(price)
print("____YOUR CART____")
for food in foods:
    print(food, end=" ")

for price in prices:
    total = total + price

print()
print(f"your total is {total}")


