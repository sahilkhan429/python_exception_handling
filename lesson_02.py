try:
    age = int(input("Enter your age: "))
    print("your age is: ", age)
except ValueError:
    print("Invalid input! Please enter a valid integer for age.")