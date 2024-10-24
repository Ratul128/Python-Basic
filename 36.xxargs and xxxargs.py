#xxargs--------------
def student(*all):
    print(all)

student("Ratul",23345,"CGPA:3.44")

def add(*addition):
    print(addition)
    sum=0
    for number in addition:
        sum=sum+number
    return sum

result=add(20,50,30)
print(result)

#xxxargs---------------------

def stud(**details):
    return details

print(stud(id=101,Name='Ratul'))
