import random
from turtledemo.minimal_hanoi import play

computer_choice= ("rock", "paper", "scissors")
running = True

while running:
    user = None
    option = random.choice(computer_choice)

    while user  not in computer_choice:
     user = str(input("pick between Rock,paper and scissors: ").lower())
    print(f"player:{user}")
    print(f"computer:{option}")



    if user == option:
        print("its a tie")
    elif user == "rock" and option == "scissors":
           print("you win")

    elif user == "paper" and option == "rock":
           print("you win")

    elif user =="scissors" and option =="paper":
           print("you win")
    else:
        print("you lose")

    run_again = str(input("play again(y/n): ").lower())
    if not run_again == "y":
        running = False



print("thanks for playing ")









