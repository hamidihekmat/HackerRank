#!/usr/bin/env python3




annual_salary = float(input('enter you annual salary: '))
portion_saved = float(input('enter the portion to be saved in decimal: '))
total_cost = float(int(input('enter the total cost of the house: ')))
portion_down_payment = total_cost * 0.25
current_savings = 0
monthly_salary = annual_salary / 12
portion_monthly = portion_saved * monthly_salary
r = 0.04
counter = 0
while current_savings <= portion_down_payment:
    current_savings = current_savings + portion_monthly + (current_savings * r/12)
    counter += 1
print(str(counter))

