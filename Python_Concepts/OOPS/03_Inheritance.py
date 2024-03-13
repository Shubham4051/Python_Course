# Child class accquire the properties and behaviour of parent class

class A:
    def displayA(self):
        print("Welcome to class A")

class B(A):
    def displayB(self):
        print("Welcome to class B")

# class C(A,B): # if not using multilevel inheritance
class C(B):
    def displayC(self):
        print("Welcome to class C")

# obj1 = B() # Single level Inheritance 
# obj1.displayA()
# obj1.displayB()
        
obj2 = C() # Multilevel Inheritance
obj2.displayA()
obj2.displayB()
obj2.displayC()