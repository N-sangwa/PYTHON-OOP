from unicodedata import name


class Account:
    def __init__(self, name,acc_number):
        self.balance = 0
        self.name = name
        self.transaction = 100
        self.acc_number = acc_number
        self.deposits = []
        self.withdrawals = []
    def deposit (self,amount):
        if amount <=0:
            return f"Deposit amount should be more than zero"

        else:    
            self.balance += amount
            self.deposits.append(f"You have deposited {amount}")
            return f"You have deposited {amount}.Your new balance is {self.balance}"
           
    def withdraw(self,amount):

        if amount > self.balance:
            return "Yout balance is {self.balance} you can not withdraw {amount}"
        elif amount <= 0:
            return f"Amount must be greater than zero"
        else:
            self.balance -= amount + self.transaction
            self.withdrawals.append (f"You have withrawn {amount}")
            return f"You have withdrawn{amount} your balance is {self.balance}"
    def deposits_statement(self):
        for statements in self.deposits:
            print(statements)
    def withdraws_statement(self):
        for staments in self.withdraws:
            print(staments)
    def current_balance(self):
        balance = self.balance
        print(balance)


   




        




        