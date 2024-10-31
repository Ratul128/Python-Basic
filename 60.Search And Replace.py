import re

pattern=r"white"
text1="white is my favourite colour. but I love blue colour as well.I have a white colour shirt, white colour pant"
#text2=re.sub(pattern,"Black",text1)
text2=re.sub(pattern,"Black",text1,count = 1) #to change a specific number of item

print(text2)