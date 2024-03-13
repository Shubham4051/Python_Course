# An obj's variable should not always be directly accessible
# the method can ensure the correct value are set. If an incorrect value is set, the method can return an error

# Getter & Setter

class Student:
    def __init__(self):
        self.__name="" # "__name" private variable.
    def getname(self):
        return self.__name
    def setname(self, name):
        self.__name=name

obj = Student()
obj.setname("Test")
name=obj.getname()
print(name)