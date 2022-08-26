class Atm:

    def __init__(self):
        self.pin = ''
        self.balance = 0
        self.menu()

    def menu(self):
        choice = int(input("""How would you like to proceed ?
            1. Create Pin 
            2. Withdraw
            3. Deposit
            4. Check Balance
            5. Exit        
        """))

        if choice == 1:
            self.create_pin()
        elif choice == 2:
            self.withdraw()
        elif choice == 3:
            self.deposit()
        elif choice == 4:
            self.check_balance()
        else:
            print("Byee See you soon!!!!!")

    def create_pin(self):
        self.pin = input("Enter your pin: ")
        print("Pin create Succesfully")

    def withdraw(self):
        wpin = input("Enter your pin")
        if wpin == self.pin:
            amount = int(input("Enter your amount: "))
            if self.balance>amount:
                self.balance = self.balance - amount
        else:
            print("Invalid pin")

    def deposit(self):
        wpin = input("Enter your pin: ")
        if wpin == self.pin:
            amount = int(input("Enter your amount: "))
            self.balance = self.balance + amount
        else:
            print("Invalid pin")

    def check_balance(self):
        print("Your Current balance is :",self.balance)


sbi = Atm()
sbi.deposit()
sbi.withdraw()
sbi.check_balance()