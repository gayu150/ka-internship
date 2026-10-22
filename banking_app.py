"""
Task 03: Banking Console Application
Kiran Academy Assignment

Author: Gayatri Bole
Date: 22/10/2026
"""

import sys

# Ensure UTF-8 output encoding for rupee symbol (₹) across all terminals
if sys.stdout.encoding and sys.stdout.encoding.lower() != "utf-8":
    try:
        sys.stdout.reconfigure(encoding="utf-8")
    except Exception:
        pass


def main():
    # Step 1: Set Opening Balance to ₹10,000.00
    balance = 10000.0

    print("Welcome to Kiran Bank")
    print(f"Opening Balance: ₹{balance:.2f}\n")

    # Step 2: Infinite loop for repeated menu display
    while True:
        print("===== KIRAN BANK =====\n")
        print("1. Check Balance")
        print("2. Deposit Money")
        print("3. Withdraw Money")
        print("4. Exit\n")

        choice = input("Enter your choice: ").strip()

        # Option 1: Check Account Balance
        if choice == "1":
            print(f"\nCurrent Balance: ₹{balance:.2f}\n")

        # Option 2: Deposit Money
        elif choice == "2":
            try:
                deposit_input = input("\nEnter deposit amount: ").strip()
                amount = float(deposit_input)

                # Validation: Deposit must be greater than zero
                if amount > 0:
                    balance += amount
                    print("\nDeposit successful!")
                    print(f"Updated Balance: ₹{balance:.2f}\n")
                else:
                    print("\nInvalid amount! Deposit must be greater than zero.")
                    print(f"Current Balance: ₹{balance:.2f}\n")
            except ValueError:
                print("\nInvalid input! Please enter a valid numeric amount.")
                print(f"Current Balance: ₹{balance:.2f}\n")

        # Option 3: Withdraw Money
        elif choice == "3":
            try:
                withdraw_input = input("\nEnter withdrawal amount: ").strip()
                amount = float(withdraw_input)

                # Validation: Must be positive and not exceed available balance
                if amount <= 0:
                    print("\nInvalid amount! Withdrawal must be greater than zero.")
                    print(f"Current Balance: ₹{balance:.2f}\n")
                elif amount > balance:
                    print("\nTransaction failed: Insufficient balance.")
                    print(f"Current Balance: ₹{balance:.2f}\n")
                else:
                    balance -= amount
                    print("\nWithdrawal successful!")
                    print(f"Updated Balance: ₹{balance:.2f}\n")
            except ValueError:
                print("\nInvalid input! Please enter a valid numeric amount.")
                print(f"Current Balance: ₹{balance:.2f}\n")

        # Option 4: Exit
        elif choice == "4":
            print("\nThank you for banking with us. Goodbye!")
            break

        # Invalid Choice Handling
        else:
            print("\nInvalid choice! Please select a valid option between 1 and 4.\n")


if __name__ == "__main__":
    main()

