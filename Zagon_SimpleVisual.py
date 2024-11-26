#!/usr/bin/env python3

# Created by: Michael Zagon
# Created on: Nov 2024
# This program displays stores sales by asterisk

# Mandatory function to display bar chart
def print_graph(store_num, store_sales):

    # // is a prebuilt python operator that divides with integral result (floor division)
    asterisks_amount = store_sales // 100

    # Prints store number and bar amount by multiplying one bar by amount needed
    print(f"Store {store_num}: {'*' * asterisks_amount}")

def main():

    # Initialization
    sales = 0
    store_num = 1 

    # While loop will proceed as long as user does not input -1
    while sales != -1:
        sales = int(input(f"Enter today's sales for store {store_num} in integer (or '-1' to quit): "))
        
        # Proceeds to print as long as user does not input -1
        if sales != -1:

            print_graph(store_num, sales)
            # Assigns store number value to previous +1
            store_num += 1

    print("\nDone.")

if __name__ == "__main__":
    main()