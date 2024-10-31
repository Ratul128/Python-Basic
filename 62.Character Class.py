
import re

#pattern= r"[aeiou]"
pattern= r"[A-Z]"
pattern= r"[0-9]"

if re.match(pattern,"673ratul"):
    print("Vowl Found")

else:
    print("Vowel not found")

