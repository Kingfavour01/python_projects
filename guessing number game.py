import random

user = int(input("can you guess the random number between 1 and 20 : "))

rand = random.randint(1 , 20)
guess = user
correct = rand == guess
while guess != rand  :
    print("wrong 🥱 try again ")
    if guess <= rand:
        print(f"you have to go higher than {guess} 😘")
        guess = int(input("try again: "))
    elif guess >= rand:
        print(f"you have to go lower than {guess} 😘 ")
        guess = int(input("try again: "))
    else:
        break

print(f"🎊 you won the answer was {guess} 🎊")




