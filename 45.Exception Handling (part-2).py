
try:
    num1=int(input("Enter 1st num:"))
    num2=int(input("Enter 2nd num:"))

    result=num1/num2
    print(result)
except (ZeroDivisionError,ValueError):
    print("incorrect Number")

finally:
    print("Thanks!")