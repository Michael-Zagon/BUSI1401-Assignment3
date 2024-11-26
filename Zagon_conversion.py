#!/usr/bin/env python3

# Created by: Michael Zagon
# Created on: Nov 2024
# This program converts Canadian dollar values into US dollar values

def main():

    print("This program converts Canadian dollar values into US dollar values.")
    #print("On November 26, 2024 at 10:33 A.M., 1 Canadian dollar is trading for 0.7097 United States dollars on the FOREX.")

    # conversion = 0.7097

    # Ask for the current exchange rate (CAD to USD)
    conversion = float(input("How many USD is 1 CAD? "))

    # Initialization
    cad = -1

    # The loop will continue as long as the user does not input 0
    while cad != 0:
        cad = float(input("Enter an amount in CAD (0 to quit): "))
        
        # Conversion will only take place if the user inputs amount that is not equal to 0
        if cad != 0:
            usd = cad * conversion
            print(f"{cad} CAD is {usd:.2f} USD")


if __name__ == "__main__":
    main()