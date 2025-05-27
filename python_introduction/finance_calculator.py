#: Use user input, variables, and arithmetic operations to calculate and provide feedback on a user’s monthly savings and potential future savings without applying conditional statements.

monthly_income = int (input("Enter your monthly income: "))
monthly_expenses = int (input("Enter your total monthly expenses: "))

monthly_savings = monthly_income - monthly_expenses

Projected_Savings = (monthly_savings * 12) + (monthly_savings * 12 * 0.05)

print("Your monthly savings is:",monthly_savings)
print("Projected savings after one year, with interest, is:",Projected_Savings)