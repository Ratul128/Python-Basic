
class Student:
    roll=""
    gpa=""

    def setValue(self,a,b):
        self.roll=a
        self.gpa=b

    def display(self):
        print(f"Roll:{self.roll}, GPA:{self.gpa}")



rahim=Student()
rahim.setValue(101,3.54)
rahim.display()
