try:
    num1 = int(input("enter first number: "))
    num2 = int(input("enter second number: "))
    result = num1/num2
    print("result is: ", result)
except ValueError:
    print("Invalid input! Please enter a valid integer.")

except ZeroDivisionError:
    print("you cannot divide by zero")