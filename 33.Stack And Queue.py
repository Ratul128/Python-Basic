
#Stack....... works as FIFO
books=[]

books.append("Learn C")
books.append("Learn Java")
books.append("Learn Python")
books.append("Learn C++")

print(books)

books.pop()
books.pop()
print(books)
'''books.pop()
books.pop()'''


if not books:
    print("No Books left")

#Queue..........works as LIFO

from collections import deque

group = deque(["Ratul", "Anis", "Munim", "Riaz"])
print(group)
group.popleft()
print(group)

group.popleft()
print(group)

group.popleft()
group.popleft()


if not group:
    print("No one left")


