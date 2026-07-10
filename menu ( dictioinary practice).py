menu = {"hotdog": 200,
        "pizza": 300,
        "drinks": 20,
        "snacks":30}

cart =[]
total = 0
print( "---------- MENU ----------" )
for key, values  in menu.items():
    print(f"{key:17}: ${values:.2f}")
print( "--------------------------" )


while True:
    food =str( input("choose an item from the menu(q to quite): ").lower())
    if food == "q":
        break
    elif menu.get(food) is not None:
        cart.append(food)

for food in cart:
    total += menu.get(food)
    print(food, end=", ")

print(f"your total is ${total:.2f}")
print("----------------------------------------------------------------")


