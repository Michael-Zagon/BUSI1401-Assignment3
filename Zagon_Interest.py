#!/usr/bin/env python3

# Created by: Michael Zagon
# Created on: Nov 2024
# This program calculates how interest rate affects users investment over 4 months

def main():

    # Welcomes the user and explains the program
    print("This program calculates how your investment will be affected by a monthly compounded annual interest rate over 4 months.")

    # Obtain values that user inputs for initial balance and annual interest rate of their investment
    user_balance = float(input("Enter the the initial value of your investment: "))
    user_interest_rate = float(input("Enter the annual interest rate on your investment in decimal form: "))

    # To convert an annual interest rate to monthly, you divide it by 12
    monthly_interest_rate = user_interest_rate / 12

    # This shows the user what they input
    print(f"\nInitial balance: {user_balance}")
    print(f"Annual interest rate in decimal: {user_interest_rate}\n")

    # Table formatting
    print("| Month | Ending Balance |")
    print("|-------|----------------|")

    # This sets the value of the current balance to the user initial input balance becuase this is the beginning
    current_balance = user_balance

    # Loop for only first 4 months
    for month in range(1, 5):

        # Calculates the current balance by multipling it by the monthly interest rate
        current_balance += current_balance * monthly_interest_rate

        # This prints the value each month in the properly formatted table
        # The numbers dictate the allighment 
        print(f"| {month:<5} | {current_balance:<14.2f} |")

    print("\nDone")


if __name__ == "__main__":
    main()