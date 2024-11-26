#!/usr/bin/env python3

# Created by: Michael Zagon
# Created on: Nov 2024
# This program displays an employees paycheck for a certain month


def main():

    print("Welcome! This program calculates your pay based off the amount of hours you worked.")

    # Gather input from the user
    employee_name = input("Enter employee name: ")
    pay_rate = float(input("Enter hourly rate: "))
    hours_worked = float(input("Enter total hours worked: "))

    # Checks if employee has worked overtime
    if hours_worked > 160:
        overtime_hours = hours_worked - 160
        regular_hours = 160
    else:
        overtime_hours = 0
        regular_hours = hours_worked

    # Calculate pay
    regular_pay = regular_hours * pay_rate # multiply hours by wage
    overtime_pay = overtime_hours * pay_rate * 1.5 # multiply overtime hours by wage and then multiply 150% (since OT)
    gross_pay = regular_pay + overtime_pay # add both pays to attain gross pay

    # Tax deduction of 10% 
    tax = gross_pay * 0.1 # tax is 10% of the gross pay
    net_pay = gross_pay - tax # subtract tax from gross pay to get employees actual earnings

    # Displays the results
    # .1f shows one decimenl place and .2f shows two decimel places
    print(f"\n{employee_name}")
    print(f"Total hours worked: {hours_worked:.1f}")
    print(f"Regular pay: {regular_pay:.2f}")
    print(f"Overtime pay: {overtime_pay:.2f}")
    print(f"Gross pay: {gross_pay:.2f}")
    print(f"Tax deduction: {tax:.2f}")
    print(f"Net pay: {net_pay:.2f}")

    print("\nDone")


if __name__ == "__main__":
    main()