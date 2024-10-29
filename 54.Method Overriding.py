
class phone:
    def __init__(self):
        print("I am phone class")

class samsung(phone):
    def __init__(self):
        super().__init__()
        print("Samsung")

obj=samsung()