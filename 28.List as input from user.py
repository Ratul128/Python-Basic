
numberWords=1
numberLetter=0
numberDigits=0

list=input("Enter the text:")

for x in list:
    x=x.lower()
    if x>='a' and x<='z':
        numberLetter=numberLetter+1
    elif x>='0' and x<='9':
        numberDigits=numberDigits+1
    elif x==" ":
        numberWords=numberWords+1

print("Total Number of Words:", numberWords)
print("Total Number of Letter:", numberLetter)
print("Total Number of Digits:", numberDigits)

