
class Trianle:
    def __init__(self,a,b):
        self.base=a
        self.height=b

    def area(self):
        result=0.5*self.base*self.height
        print(result)

t1=Trianle(20,30)
t2=Trianle(10,20)

t1.area()
t2.area()