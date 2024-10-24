
num1={1,2,5,5,4,10,19,7}
print(num1)

num2=set([9,2,8,1])
print(num2)

num2.add(199)
num2.remove(1)
print(num2)

print(num1|num2) #union
print(num1&num2) #intersection
print(num1-num2) #difference

