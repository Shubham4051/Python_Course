# Getter & Setter

class Student:
    def __init__(self):
        self.__name=""
    def getname(self):
        return self.__name
    def setname(self, name):
        self.__name=name

obj = Student()
obj.setname("Test")
name=obj.getname()
print(name)