
def add(*addition):
    print(addition)
    sum=0
    for number in addition:
        sum=sum+number
    return sum

print(add(20,10,5,10,5))