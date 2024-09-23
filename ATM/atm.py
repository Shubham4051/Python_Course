class Atm:

    def __init__(self) :
        self.pin = ''
        self.balance = 0
        
        self.menu()

    def menu(self):
        user_input = int(input('''
                               Hello, how can I help you ? Press :
                               1 for pin creation
                               2 for balance check
                               3 for withdrawl
                               4 for deposit
                               5 for exit
'''))
        if user_input == 1:
            self.create_pin()
        
        if user_input == 2:
            self.check_balance()
        
        if user_input == 3:
            self.withdraw()
        
        if user_input == 4:
            self.deposit()
        
        if user_input == 5:
            print("Bye")
            
    def create_pin(self):
        pin = int(input("Create your pin : "))
        print("Pin set Successfully")

    def check_balance(self):
        temp = int(input("Enter your pin"))
        if temp == self.pin:
            pass
        else:
            print("Incorrect Pin")