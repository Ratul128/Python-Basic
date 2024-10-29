
from abc import ABC, abstractmethod
class shape(ABC):
    def __init__(self,base, height):
        self.dim1=base
        self.dim2=height

    @abstractmethod
    def area(self):
        pass

class triangle(shape):
    def area(self):
        result=0.5*self.dim1*self.dim2
        return result

class ractangle(shape):
    def area(self):
        result=self.dim1*self.dim2
        return result


obj1=ractangle(20,30)
print(obj1.area())
obj2=triangle(20,30)
print(obj2.area())