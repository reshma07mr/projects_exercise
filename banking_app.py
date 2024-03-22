#This is a banking app implementation using the class concept of Python.

class Bank:
    def __init__(self):
        pass

    def details_fn(self,name, account_number, balance):
        self.name = name
        self.account_number =  account_number
        self.balance = balance
        
    def display_details(self):
        print(self.name)
        print(self.account_number)
        print(self.balance)

    def deposit_fn(self, amount):
        self.balance += amount

    def withdraw_fn(self,withdraw_amount):
        self.balance -= withdraw_amount     

object = Bank()
name = input('Enter the name of the account holder :')
account_number = input("Enter the account number : ")
balance = input("enter the balance required :")
amount = input("enter the amount to be deposited")


print("Select the functionality :\n 1. Display the information. \n 2. Deposit cash. \n 3. Withdraw cash. ")
choice = input("enter the choice : ")

if choice == 1:
    object.details_fn(name,account_number, balance)
    object.display_details()

if choice == 2:
    object.deposit_fn(amount)
    object.display_details()

if choice == 3:  
    object.withdraw_fn(withdraw_amount)
    object.display_details()


else :
    print("Invalid choices made. retry again.")    
