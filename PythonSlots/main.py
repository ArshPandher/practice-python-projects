import random


def spin_row():
    symbols = ['🍒', '🍋', '⭐', '🔔', '🍉']
    results = []

    for symbol in range(3):
        results.append(random.choice(symbols))

    return results


def print_row(row):
    print(" | ".join(row))


def get_payout(row,bet):
    if row[0] == row[1] == row[2]:
        if row[0] == '🍒':
            return bet * 2
        if row[0] == '🍋':
            return bet * 3
        if row[0] == '⭐':
            return bet * 5
        if row[0] == '🔔':
            return bet * 10
        if row[0] == '🍉':
            return bet * 20
    return 0

def main():
    balance = 100

    while balance > 0:
        print("********************")
        print(" PYTHON SLOTS GAME ")
        print("SYMBOLS: 🍒🍋⭐🔔🍉")
        print("********************")
        print(f"Your balance is: ${balance}")

        bet = input("Enter your bet: $")

        if not bet.isdigit():
            print("Please enter a valid bet!")
            continue

        bet = int(bet)

        if bet > balance:
            print("Insufficient funds!")
            continue

        if bet <= 0:
            print("Bet should be greater than zero!")
            continue

        print("Spinning....")

        row = spin_row()
        print_row(row)
        balance -= bet

        payout = get_payout(row, bet)

        if payout > 0:
            print(f"You won ${payout}")

        else:
            print("You lost this round!")

        balance += payout

        play_again = input("Do you wish to play again(Y/N): ").upper()

        if not play_again == 'Y':
            break

if __name__ == "__main__":
    main()