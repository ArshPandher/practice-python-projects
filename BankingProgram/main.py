def show_balance(balance):
    print(f"Your balance is: ${balance:.2f}")

def deposit():
    amount = float(input("Enter the amount to be deposited: $"))

    if amount < 0:
        print("Amount cannot be less than zero")
        return 0
    else:
        return amount

def withdraw(balance):
    amount = float(input("Enter the amount to be withdrawn: $1"))

    if amount < 0:
        print("Amount cannot be less than zero")
        return 0
    elif amount > balance:
        print("INSUFFICIENT FUNDS!")
        return 0
    else:
        return amount


def main():
    balance = 0
    is_running = True

    while is_running:
        print("**********************")
        print("PYTHON BANKING PROGRAM")
        print("**********************")
        print("Choose an option:")
        print("1.Show balance")
        print("2.Deposit")
        print("3.Withdraw")
        print("4.Exit")

        choice = input("Enter your choice(1-4): ")

        match choice:
            case '1':
                show_balance(balance)
            case '2':
                balance += deposit()
            case '3':
                balance -= withdraw(balance)
            case '4':
                is_running = False
                print("THANKS! HAVE A NICE DAY!")
            case _:
                print("Invalid Input!")



if __name__ == '__main__':
    main()
