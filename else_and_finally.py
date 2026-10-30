try:
    income = float(input("Enter monthly income: "))
    expenses = float(input("Enter monthly expenses: "))
    if income < 0 and expenses < 0:
        raise ValueError("Income and expenses cannot be negative.")
except ValueError as error:
    print("error:",error)

else:
    balance = income - expenses
    print("Your monthly balance is: ", balance)

finally:
    print("expense calculation completed.")