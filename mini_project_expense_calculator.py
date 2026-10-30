try:
    income = float(input("Enter your income: "))
    expenses = float(input("Enter your expenses: "))
    savings = income - expenses
    print("Your savings are: ", savings)
except ValueError:
    print("Invalid input! Please enter a valid number for income and expenses.")
    