
#HIERARCHICAL INHERITENCE

'''class shape:
    def __init__(self,base,height):
        self.dim1=base
        self.dim2=height


class triangle(shape):
    def area(self):
        area1= 0.5*self.dim1*self.dim2
        return area1

class ractangle(shape):
    def area_ractangle(self):
        area2=self.dim1*self.dim2
        return area2



obj1=triangle(10,20)
obj2=ractangle(20,10)

print(obj1.area())
print(obj2.area_ractangle())'''

#MULTILEVEL INHERITENCE
'''class A:
    def display1(self):
        print("I am in class A")

class B(A):
    def display2(self):
        print("I am in class B")

class C(B):
    def display3(self):
        super().display1()
        super().display2()
        print("I am in class C")

obj1=C()
obj1.display3()'''

#MULTIPLE INHERITENCE

class A:
    def display1(self):
        print("I am in class A")

class B:
    def display2(self):
        print("I am in class B")

class C(A,B):
    def display3(self):
        print("I am in class C")

obj1=C()
obj1.display1()
obj1.display2()
obj1.display3()