annual_salary = float(input("Enter your annual salary: "))
portion_saved = float(input("Enter the percent of your salary to save, as a decimal: ")) #dedicated amount from salary
total_cost = float(input("Enter the cost of your dream home: "))

current_savings = 0
portion_down_payment = 0.25
r = 0.04 #return on savings investment
monthly_salary = float(annual_salary/12)
months = 0

while current_savings < (total_cost*.25):
    current_savings += float((current_savings*(0.04/float(12))) + (monthly_salary*portion_saved))
    months += 1

print(current_savings)
print("Number of months:", months)

