mark= int(input("Enter the mark:"))

if 80<=mark<=100:
    print("A+")

elif 70<=mark<=79:
    print("A")

elif 60<=mark<=69:
    print("A-")

elif 50<=mark<=59:
    print("B")

elif 40<=mark<=49:
    print("D")

elif 0<=mark<=39:
    print("F")

else:
    print("Mark is invalid")