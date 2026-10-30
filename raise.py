amount = float(input("Enter expense amount: "))
if amount < 0:
    raise ValueError("Expense amount cannot be negative.")
print("Expense amount is: ", amount)