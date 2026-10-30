try:
    number  = 10
    result = number/0
    print(result)

except ZeroDivisionError:
    print("you cannot divide by zero")

print("Programm continues...")