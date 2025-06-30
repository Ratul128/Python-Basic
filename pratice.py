'''abc=int(input("Enter the value of n:"))

xyz=range(1,abc+1,1)

sum=0
for x in xyz:
    sum=sum+x*x
print(sum)'''
from lib2to3.pygram import pattern_grammar

'''from random import randint



for x in range (1,6):
    ratul = int ( input ( "enter the guess number:" ) )
    yakin = randint ( 1 , 10 )
    if ratul==yakin:
        print("You Won")
        break
    else:
        print("You lost")
        print("The random number is:",yakin)
print("Game is over")'''

'''x=input("Enter the value: ")
l=x.split()
s=0
for i in l:
    s=s+int(i)
print(s)'''

'''now=1
nol=0
nod=0

k=input("Enter The text:")
k=k.lower()

for x in k:
    if x>='a' and x<='z':
        nol=nol+1
    elif x>='0' and x<='9':
        nod=nod+1
    elif x==" ":
        now=now+1

print("Total Number of Words:",now)
print("Total Number of Letters:",nol)
print("Total Number of Digits:",nod)'''

'''mt=[
    [1,2,3],
    [4,5,6]
]

#print(mt[1][1])

for x in mt:
    for y in x:
        print(y)'''

'''taak={
    "tk1":"Ratul",
    "tk2":"Anas",
    "tk3":"Jahir",
    "tk4":"Mehedi"
}

print(taak.get("tk7","Not a valid key"))'''

'''tuples=(
    ("ratul", "tutul", 343),
    "anas",
    "jahir",
    "mehedi",
    "hasan",
    "tutul",
    "afrin",
    "tuhin",
    1234
)

print(tuples)
print(tuples[2])
print(tuples[1:5+1])
print(tuples[1:])
print(tuples[0][1])'''

'''set_up={10,20,11,21,30,40,31,41,1,1,1}
print(set_up)

set_up2=set([10,50,11,30])
set_up2.add(40)
#set_up2.remove(11)
print(set_up2)

union=set_up | set_up2
print(union)

print(set_up&set_up2)

print(set_up-set_up2)'''

'''mystack = []
mystack.append("BA")
mystack.append("IA")
mystack.append("Math")
print(mystack)
mystack.append("English")
mystack.append("Bangla")
mystack.append("Physics")

mystack.pop()
if not mystack:
    print("No Books left")
else:
    print(mystack)
#print("Now the top book is: ", mystack[-1])
mystack.pop()
if not mystack:
    print("No Books left")
else:
    print(mystack)
mystack.pop()
if not mystack:
    print("No Books left")
else:
    print(mystack)
print(mystack)
mystack.pop()
print(mystack)
mystack.pop()
print(mystack)
mystack.pop()
if not mystack:
    print("No Books left")'''

'''from collections import deque
my_que=deque(["Ratul", "Anis", "Munim"])
print(my_que)

my_que.popleft()
if not my_que:
    print("No one left")
else:
    print(my_que)

my_que.popleft()
if not my_que:
    print("No one left")
else:
    print(my_que)

my_que.popleft()
if not my_que:
    print("No one left")
else:
    print(my_que)'''


#Function:
'''def add(x,y):
    sum=x+y
    print(sum)

def sub(x,y):
    sub=x-y
    print(sub)

def add2(x,y,z):
    sum=x+y+z
    print(sum)

add(10,20)
sub(30,20)
add2(10,20,30)'''

'''def addition(x,y):
    sum=x+y
    return sum
print(addition(20,30))

def large(x,y):
    if x>y:
        return x
    else:
        return y
compare=large(200,30)
print(compare)'''

'''def tt(*all):
    print(all[1])

tt(23, "ratul", 3.66)'''

'''def tt2(*all):
    sum=0
    for x in all:
        sum=sum+x
    print(sum)
tt2(10,20,30,40,50)'''

'''def tt3(**all):
    print(all["Age"])

tt3(Name="Ratul", Age=23, Height=5.6)'''

'''try:
    list=[20,0,30,40]
    result= list[0]/list[a]
    print(result)
    print("Done")

except ZeroDivisionError:
    print("Dividing by 0 is not possible")

except IndexError:
    print("list index out of range")

finally:
    print("Successful")'''

'''class Brother:
    roll=""
    gpa=""
abc=Brother()
#print(isinstance(abc,Brother))

abc.roll=101
abc.gpa=3.54
print(f"abc's Roll is:{abc.roll} Rahim's GPA is:{abc.gpa}")

xyz=Brother()

xyz.roll=102
xyz.gpa=3.22
print(f"xyz's Roll is:{xyz.roll} Rahim's GPA is:{xyz.gpa}")'''

'''class Car:
    def __init__(self,name,color,year):
        self.name=name
        self.color=color
        self.year=year

    def show_car_info(self):
        print(f"Car:{self.name}, Color:{self.color}, Year:{self.year}")

audi=Car("Toyota","Red",2020)

audi.show_car_info()'''

'''class Triangle:
    def __init__(self,bs,ht):
        self.base=bs
        self.height=ht

    def calculate_area(self):
        print(f"Area of Triangle is: {0.5*self.base*self.height}")

cal=Triangle(20,30)
cal.calculate_area()

cal2=Triangle(10,20)
cal2.calculate_area()'''


'''class Vehicle:
    def start_engine(self):
        print("Vehicle engine started")

class Car(Vehicle):
    def start_engine(self):
        super().start_engine()
        print("Car engine started")

class Bike(Vehicle):
    def start_engine(self):
        super().start_engine()
        print("Bike engine started")

a=Car()
a.start_engine()
b=Bike()
b.start_engine()'''

'''class Shape:
    def area(self):
        print("Can not defined area")

class Rectangle(Shape):
    def area(self,length,width):
        self.'''

import re

'''ptrn=r"color"
text1="Red is my favourite color. I love red color most. Black color and white color also favourite to me"

text2=re.sub(ptrn,"colourrr",text1,count = 2)
print(text2)'''







