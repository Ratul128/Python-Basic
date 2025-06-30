#Task-1:
'''একটি Vehicle class তৈরি করো যার একটি method থাকবে start_engine() নামে। এরপর দুটি subclass বানাও:
Car: override করে বলবে "Car engine started"
Bike: override করে বলবে "Bike engine started"
তারপর Car এবং Bike এর object বানিয়ে start_engine() call করে দেখো।'''

'''class Vehicle:
    def start_engine(self):
        print("Vehicle engine started")

class Car(Vehicle):
    def start_engine(self):
        super().start_engine()
        print("Car engine started")

class Bike(Vehicle):
    def start_engine(self):
        super().start_engine()
        print("Bike engine started")

a=Car()
a.start_engine()
b=Bike()
b.start_engine()'''

'''Practice Task 2:
একটি class বানাও Shape নামে। তার একটি method থাকবে area() যেটা বলবে "Cannot define area".
এরপর দুটি subclass বানাও:
Rectangle: override করে area() method-এ দৈর্ঘ্য × প্রস্থ return করবে।
Circle: override করে area() method-এ π × r² return করবে।
Extra: ইউজার থেকে input নাও দৈর্ঘ্য/প্রস্থ বা radius!
'''
'''class Shape:
    def area(self):
        print("Cannot define area")
class Rectangle(Shape):
    def area(self,length,width):
        area1=length*width
        return area1
class Circle(Shape):
    def area(self,radius):
        area2=3.1416*radius*radius
        return area2

rctngle=Rectangle()
abc=(rctngle.area(int(input("Enter The length:")),int(input("Enter the width:"))))

crcle=Circle()
xyz=(crcle.area(int(input("Enter the value of radius:"))))

print(f"The area of Rectengle is: {abc}")
print(f"The are of circle is: {xyz}")'''

'''Practice Task 3:
Phone নামে একটি class বানাও যার একটি method থাকবে features()।
এরপর দুটি subclass বানাও:
BasicPhone: override করে বলবে "Can only call and text"
SmartPhone: override করে বলবে "Can use internet, apps, camera"
super() ব্যবহার করে parent এর message + child এর message একসাথে প্রিন্ট করো।'''

'''class Phone:
    def features(self):
        print("this message is for phone")

class BasicPhone(Phone):
    def features(self):
        super ( ).features ( )
        print("can only call and text")

class SmartPhone(Phone):
    def features(self):
        super ( ).features ( )
        print("can use internet, apps, camera")
phn=BasicPhone()
phn.features()
smrt=SmartPhone()
smrt.features()'''



