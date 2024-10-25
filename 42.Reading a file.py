
file=open("student.txt","r+")
print(file.readable())

'''txt=file.read()
print(txt)


size= len ( txt )
print(size)'''

size=file.readlines()[1]
print(size)
file.close()


