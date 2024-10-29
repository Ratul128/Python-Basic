
class phone:  #parent class/main class
    def call(self):
        print("You can call")

    def messenger(self):
        print("You can message")


class samsung(phone): #sub class/child class
    def photo(self):
        print("You can send photo")


obj1=samsung()
obj1.call()
obj1.messenger()
obj1.photo()

print(issubclass(samsung,phone))