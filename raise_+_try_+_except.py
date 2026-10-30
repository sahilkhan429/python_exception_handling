try:
    amount = float(input("Enter expense amount: "))
    if amount < 0:
        raise ValueError("Expense amount cannot be negative.")
except ValueError as error:
    print("Invalid input:", error)

else:
    print("Expense amount is: ", amount)

finally:
    print("Expense processing completed.")