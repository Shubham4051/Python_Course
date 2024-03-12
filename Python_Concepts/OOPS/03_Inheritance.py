# Child class accquire the properties and behaviour of parent class

class A:
    def displayA(self):
        print("Welcome to class A")


class B(A):
    def displayB(self):
        print("Welcome to class B")

obj1 = B() # Single level Inheritance 
obj1.displayB()
obj1.displayA()