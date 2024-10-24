num=[1,2,3,4,5]

#expression for item in list

result1=[x*x for x in num]
print(result1)

result2=[x for x in num if x%2==0]
print(result2)