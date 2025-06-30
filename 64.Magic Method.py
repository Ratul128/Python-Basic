#__init__(self, ...) → Constructor
class Person:
    def __init__(self, name):
        self.name = name

p = Person("Mehedi")
print(p.name)

#__str__(self) → Human-readable string রিটার্ন করে
class Person:
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return f"Person's name is {self.name}"

p = Person("Mehedi")
print(p)  # Output: Person's name is Mehedi

#__add__(self, other) → + অপারেটর কাস্টমাইজ
class Number:
    def __init__(self, value):
        self.value = value

    def __add__(self, other):
        return self.value + other.value

n1 = Number(10)
n2 = Number(20)
print(n1 + n2)  # Output: 30

#__len__(self) → len() ফাংশনের behavior define করে
class MyList:
    def __init__(self, items):
        self.items = items

    def __len__(self):
        return len(self.items)

l = MyList([1, 2, 3])
print(len(l))  # Output: 3


