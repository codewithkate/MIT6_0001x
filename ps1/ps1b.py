"""
Write a program to calculate how many months it will take you save up enough money for a down
payment. Like before, assume that your investments earn a return of r = 0.04 (or 4%) and the
required down payment percentage is 0.25 (or 25%).
"""

def invest(current_savings):
    """
    Input: two float values
    Return monthly return on investment
    """
    r = 0.04 # annual return
    return current_savings*r/12

def save(portion_saved, annual_salary):
    """
    Input: two float values
    Return portion of monthly salary
    """
    return annual_salary/12 * portion_saved


# Retrieve user input
annual_salary = float(input("Enter your annual salary: "))
portion_saved = float(input("Enter the percent of your salary to save, as a decimal: "))
total_cost = float(input("Enter the cost of your dream home: "))
semi_annual_raise = float(input("Enter the semi-­annual raise, as a decimal: "))

# Calculating how much to save
portion_down_payment = 0.25
down_payment = total_cost * portion_down_payment

# Determine how many months of saving
current_savings = 0
months = 0
while down_payment > current_savings:
    if months != 0 and months % 6 == 0:
        annual_salary += annual_salary * semi_annual_raise
    current_savings += invest(current_savings) + save(portion_saved, annual_salary)
    months += 1

print('Number of months:', months)