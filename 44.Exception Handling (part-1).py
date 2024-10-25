
try:
    list=[20,0,30,40]
    result= list[0]/list[a]
    print(result)
    print("Done")

except ZeroDivisionError:
    print("Dividing by 0 is not possible")

except IndexError:
    print("Index Error")

finally:
    print("Successful")