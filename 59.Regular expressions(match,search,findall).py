import re

pattern=r"colour"

#match() function---------------------------------
'''if re.match(pattern,"Red is color I hlove the most"):
    print("Matched")

else:
    print("Not matched")'''


#search() function----------------------------------
'''if re.search(pattern,"I have a black colour pant only. 
I used it so many times because I have no other options left "):
    print("Matched")

else:
    print("Not matched")'''

#findall() -----------------------------------------

print(re.findall(pattern,"I have a black colour pant only. "
                         "I used it so many times because I have no other options left.black is my fav colour"))

#start,end,span method -------------------------------------

text= "My favourite colour is white"

match= re.search(pattern,text)
if match:
    print(match.start())
    print(match.end())
    print(match.span())