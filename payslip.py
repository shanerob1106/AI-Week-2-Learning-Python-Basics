# Constant variables 
tax_rate = 0.4
threshold = 11000

# Data entry
name = input("Please enter your name: ")
entry = input("Please enter your salary: ")

# Tax calculations
salary = int(entry)
tax_payable = (salary - threshold) * tax_rate
pay = salary - tax_payable

# Final output
print("Payslip for: ", name)
print("Salary: ", salary)
print("Minus taxes", tax_payable)
print("Take home salary: ", pay)

