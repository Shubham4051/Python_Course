# Overloading & Overriding
# Polymorphism - same fn (diff signature) being use for diff types

# l = [10, 20, 30, 40] ; s= "welcome" # str vs int same output in int
# print(len(l)) ; print(len(s))

# Overloading - same fn diff parameter and output
class Sam:
    def displayinfo(self, name=''):
        print("Welcome to reality " + name)

# obj1 = Sam()
# obj1.displayinfo()
# obj1.displayinfo("Shubham")

# Overriding - child override the member of parent class with same name . 
class Sam:
    def display_name(self):
        print("Hello Sam")

class Work(Sam):
    def display_name(self):
        super().display_name()
        print("Welcome to the reality.")

obj2 = Work()
obj2.display_name()
# Super fn is used to call member of parent class with same name