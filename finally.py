try:
    amount = int(input("Enter expense amount: "))
    print("Expense amount is: ", amount)
except ValueError:
    print("Invalid input! Please enter a valid integer for expense amount.")

finally:
    print("expense processing finished:")

    