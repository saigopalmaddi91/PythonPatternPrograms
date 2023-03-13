class Customer:
    """ This is a simple bank application with basic operations """

    bank_name = "TD Bank"  # static variable

    def __init__(self, name, balance=0.0):
        # Instance variables
        self.name = name
        self.balance = balance

    def deposit(self, amount):
        self.balance = self.balance + amount
        print("Amount deposited Successfully, Your new balance is : ", self.balance)

    def withdraw(self, amount):
        if amount > self.balance:
            print("Insufficient Funds, This operation cannot be performed......")

        else:
            self.balance -= amount
            print("Amount withdrawn Successfully, Your new balance is : ", self.balance)


print("Welcome to ", Customer.bank_name)
name = input("Enter Your Name : ")
c = Customer(name)

while True:
    print(f" Hello {c.name}, Enter d for Deposit \n w for Withdraw \n  e for exit")
    choice = input("Enter your choice : ").lower()

    if choice == 'd':
        amount = eval(input("Enter amount to deposit : "))
        c.deposit(amount)
    elif choice == 'w':
        amount = eval(input("Enter amount to withdraw : "))
        c.withdraw(amount)
    elif choice == 'e':
        print("Thank you for banking with us")
        break
    else:
        print("Invalid choice, kindly select valid operation")
