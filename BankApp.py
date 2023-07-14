class Customer:
    """ This is Bank Application by Rajesh """
    bankName = "RajBank"
    def __init__(self,name,balane = 0.0):
        self.name = name
        self.balance = balane
    def deposit(self,amount):
        self.balance = self.balance + amount
        print("After deposit balance is :",self.balance)
    def withdraw(self,amount):
        if self.balance < amount :
            print("Insufficient funds")
        else:
            self.balance = self.balance - amount
            print("Balance after withdraw is :",self.balance)

print("Welcome to ",Customer.bankName)

name = input("Enter name")
c = Customer(name)
while True:
    print("d-deposit\nw-withdraw\ne-exit")
    option = input("Enter your option:")
    if option.lower() == 'd':
        amount = float(input("Enter amount to deposit:"))
        c.deposit(amount)
    elif option.lower() == 'w':
        amount = float(input("Enter amount to Withdraw:"))
        c.withdraw(amount)
    elif option.lower() == 'e':
        print("Thank you for banking with ",Customer.bankName)
        break
    else:
        print("Invalid option, enter proper input")








