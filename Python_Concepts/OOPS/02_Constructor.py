# Constructor is a method, call itself
class DemoClass2:
    a = 50
    def __init__(self): # Constructor call on itself
        print("Welcome to Constructors")

    def showvalue(self):
        # print(self.a) # self.a use to call undeclared variable outside the method

        c = self.a * self.a - 100
        print(c)

    def showstatement(self, a, b):
        print("Great Concept")
        print(a + b)



obj1 = DemoClass2() 

obj1.showvalue()

obj1.showstatement(20, 90)