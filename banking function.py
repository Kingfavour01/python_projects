


def show_balance(balance) :
    print("***************************************")
    print(f"your balance is ${balance:.2f}")


def deposit():
     amount = float(input("enter your amount: "))
     if amount < 0:
        print("***************************************")
        print("this is invalid amount ")
        print("***************************************")
        return 0
     else:
          return amount
def withdraw(balance):
    amount = float(input("enter amount you want to withdraw: "))

    if amount > balance:
        print("***************************************")
        print("insufficient funds")
        print("***************************************")
        return 0
    elif amount <=0:
        print("***************************************")
        print("you cannot withdraw a negative amount")
        print("***************************************")
        return 0
    else:
        return amount
def main():
    balance = 0
    is_running = True
    while is_running:
        print("***************************************")
        print("banking program")
        print("***************************************")

        print("enter 1 (for balance)")
        print( "enter 2 (for deposit)")
        print( "enter 3 (for withdraw)")
        print("enter 4 to quite")
        print("***************************************")

        choice = input("Enter from (1-4): ")
        if choice == "1":
            show_balance(balance)
        elif choice == "2":
            balance +=deposit()
        elif choice == "3":
           balance -= withdraw(balance)
        elif choice == "4":
            is_running = False
        else:
            print("***************************************")
            print("invalid choice")
            print("***************************************")
    print("***************************************")
    print("thank you have a nice day ")
    print("***************************************")


if __name__ == "__main__":
    main()









