class Account:
    def __init__(self, amount_withdrawn, balance, account_name, amount_deposited):
        self.amount_withdrawn = amount_withdrawn
        self.balance = 0
        self.amount_deposited = amount_deposited
        self.account_name = account_name
        self.balance += amount_deposited
       

    def deposit(self):
        return f"Hello {self.account_name}, you have deposited {self.amount_deposited}, your new balance is {self.balance + self.amount_deposited}" 
    def withdrawals(self):
        return f"Hello {self.account_name}, you have withdrawn {self.amount_withdrawn}, your new balance is {self.amount_deposited - self.amount_withdrawn}"

        
    