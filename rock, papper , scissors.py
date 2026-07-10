import random
user = None
computer_choice= ("rock", "paper", "scissors")
option = random.choice(computer_choice)
#print(option)
while user  not in computer_choice:
 user = str(input("pick between Rock,paper and scissors: ").lower())
print(f"player:{user}")
print(f"computer:{option}")


while True:
   if user == "rock" and option == "rock":
       print("its a tie ")
       break
   elif user == "scissors" and option == "scissors":
       print("its a tie ")
       break
   elif user == "paper" and option == "paper":
       print("its a tie ")
       break
   elif user == "rock" and option == "scissors":
       print("you win")
       break
   elif user == "paper" and option == "rock":
       print("you win")
       break
   elif user =="scissors" and option =="paper":
       print("you win")
       break
   elif user == "rock" and option == "paper":
       print("you lose")
       break
   elif user == "paper" and option == "scissors":
       print("you lose")
       break
   else:
       user == "scissors" and option == "rock"
       print("you lose")
       break

# I just realised that I could have just done user==option for tie part








