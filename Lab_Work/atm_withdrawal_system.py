# 7. ATM Withdrawal System

def atm_system():
    balance = 10000

    while True:
        print(f"\nCurrent Balance = {balance}")

        withdrawal_amount = float(input("Enter withdrawal amount: "))

        if withdrawal_amount < 0:
            print("Invalid Amount")
        elif withdrawal_amount > balance:
            print("Insufficient Balance")
        else:
            balance = balance - withdrawal_amount
            print("Withdrawal Successful")
            print(f"Remaining Balance = {balance}")

        choice = input("Do you want to continue? (yes/no): ").lower()

        if choice == "no":
            print("Thank You for Using ATM")
            break

atm_system()
