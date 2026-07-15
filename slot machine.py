import random


def spin_row():
    symbols = ["🍒", "🍉", "🍋", "🔔", "⭐"]
    return [random.choice(symbols) for _ in range(3)]


def print_row(row):
    print("**********************************")
    print(" | ".join(row))
    print("**********************************")


def get_payout(row, bet):
    if row[0] == row[1] == row[2]:
        if row[0] == "🍒":
            return bet * 3
        elif row[0] == "🍉":
            return bet * 4
        elif row[0] == "🍋":
            return bet * 5
        elif row[0] == "🔔":
            return bet * 10
        elif row[0] == "⭐":
            return bet * 20
    return 0


def main():
    balance = 100
    print("**********************************")
    print("welcome to python slot")
    print("SYMBOLS: 🍒🍉🍋🔔⭐")
    print("*********************************")

    while balance > 0:
        print(f"current balance ${balance}")

        bet = input("place your bet amount: ")

        if not bet.isdigit():
            print("please enter a valid number: ")
            continue

        bet = int(bet)

        if bet > balance:
            print("insufficient fund")
            continue
        if bet <= 0:
            print("insufficient fund")

        balance -= bet

        row = spin_row()
        print("spinning..........\n")
        print_row(row)

        payout = get_payout(row, bet)

        if payout > 0:
            print(f"you won ${payout}")
        else:
            print(f"sorry you lost that round")

        balance += payout

        play_again = input("do you want to play again(Y/N): ")

        if play_again.upper() != "Y":
            break
    print("****************************************")
    print(f"game over! your balance is ${balance} ")
    print("****************************************")


if __name__ == '__main__':
    main()
