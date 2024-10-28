
class Student:
    roll=""
    gpa=""

    def __init__(self,a,b):
        self.roll=a
        self.gpa=b

    def display(self):
        print(f"Roll:{self.roll}, GPA:{self.gpa}")

rahim=Student(101,3.54)
karim=Student(105,3.88)

rahim.display()
karim.display()
