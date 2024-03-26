class Rent_bike:
    def __init__(self,stock):
        self.stock=stock
    def displayBike(self):
        print("Total no. of bikes present",self.stock)
    def rentForBike(self, q):

        if(q <= 0):
            print("Enter the positive value ")
        elif q > self.stock:
            print("Enter Valid Quantity in the stock")
        else:
            self.stock=self.stock-q
            print("Total price", q*100)
            print("Total Bikes", self.stock)

while True:
    obj = Rent_bike(100)
    uc = int(input('''
                   1. Display Stock
                   2. Rent Bike
                   3. Exit \n''' ))
    
    if uc == 1:
        obj.displayBike()
    elif uc == 2:
        n = int(input("Enter the Quantity :----"))
        obj.rentForBike(n)
    else:
        break