class DemoClass: # Creating Class
    a = 10

    def sumvalue(self): # self is an argument acting as an Object
        print(20 + 30)



demoObj = DemoClass() # Creating Object
# Can create Multiple Objects
# demoObj1 = DemoClass()

print(demoObj.a) # Calling Variable of a class
# print(demoObj.a + 10) # Through another Object 

# 1 class can have multiple objects
# obj are made outside the class 

# method are defined inside a class and functions can also be defined outside a class

demoObj.sumvalue()