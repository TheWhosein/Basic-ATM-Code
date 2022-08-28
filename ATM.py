

class bank:
    def __init__(self, name, balance):
        self.name=name
        self.status=True
        self.balance = balance
        
    def run(self):
        self.menu()
        choice=self.choice()
        
        if choice==1:
            self.put()
        if choice==2:
            self.withdraw()
        if choice==3:
            self.show()
        if choice==4:
            self.donate()
        if choice==5:
            self.rate()
        if choice==6:
            self.exitSystem()
        
    def menu(self):
        print("**** Welcome to the ***** bank ****")
        print("\n1)Put your money on the card\n2)Withdraw money from the card\n3)Show balance of the card\n4)Donate our bank for helping to disabled people\n5)Rate us\n6)Exit\n")
        
    def choice(self):
        while True:
            try:
                process=int(input("Select:"))
                if process<1 or process>6:
                    print("Operation number must be between 1-6, please correct number.\n")
                    continue
                break
            except ValueError:
                print("Operation is must be integer number, please write correct type.\n")
                
        return process
    def put(self):
        money = int(input("Please put the money in the ATM\n"))
        self.balance = self.balance + money
     
    def withdraw(self):
        if self.balance > 0:
            money = int(input("How much money do you want to cash\n"))
            if self.balance < money:
                print("You don't have that much money in your account\n")
            else:
                self.balance = self.balance - money
        elif self.balance == 0:
            print("You have no money on your account\n")
        
    def show(self):
       print(self.balance)
    
    def donate(self):
        if self.balance > 0:
            donate = int(input("How much money do you want to donate for disabled people?\n"))
            if self.balance < donate:
                print("You don't have that much money in your account\n")
            else:
                self.balance = self.balance - donate
        elif self.balance == 0:
            print("You have no money on your account\n")
        
        print("\nThanks for donation\n")
    
    def rate(self):
        while True:
            try:
                rate = int(input("Rate our customer recommendation(0-5):\n"))
                if rate < 1 or rate > 6:
                    print("Operation number must be between 0-5, please correct number.\n")
                    continue
                break
            except ValueError:
                print("Operation is must be integer number, please write correct type.\n")
            
        
    def exitSystem(self):
        self.status=False
        
    
    
balance = 0
ATM=bank("***** BANK", balance)

while ATM.status:
    ATM.run()