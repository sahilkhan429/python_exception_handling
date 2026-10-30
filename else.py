try:
    income = float(input("Enter your income: "))
    print("Icome is: ", income)
except ValueError:
    print("Invalid input! Please enter a valid number for income.")

else:
    print("Income entered successfully.")