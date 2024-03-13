# Hiding non essential parts 
class Students:
    __name = "Sam"

    def __init__(self): # Constructor to call itself
        print(self.__name)
        self.__displayscl()

    def __displayscl(self):
        print("Welcome to TITS.")

obj = Students()
# print(obj.__name)
# constructor call itself