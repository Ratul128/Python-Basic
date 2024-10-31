import re
def pat1(pattern,text):
    if re.match(pattern,text):
        print("Matched")
    else:
        print("Not matched")
def pat2(pattern,text):
    if re.match(pattern,text):
        print("Matched")
    else:
        print("Not matched")
def pat3(pattern,text):
    if re.match(pattern,text):
        print("Matched")
    else:
        print("Not matched")
def pat4(pattern,text):
    if re.match(pattern,text):
        print("Matched")
    else:
        print("Not matched")
def pat5(pattern,text):
    if re.match(pattern,text):
        print("Matched")
    else:
        print("Not matched")
def pat6(pattern,text):
    if re.match(pattern,text):
        print("Matched")
    else:
        print("Not matched")

pat1(r"Bla.k","Black is my fav colour")
pat2(r"^Bla........k$","Black is myk")
pat3(r"a*","aBlack is my fav colour")
pat4(r"a+","aBlack is my fav colour")
pat5(r"ice(-)?cream","icecream is my most favourite")
pat6(r"a{1,3}$","aa")

