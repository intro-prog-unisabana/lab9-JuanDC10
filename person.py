# person.py
class Person: 
    def __init__(self, name, accounts):
        self.name = name 
        self.accounts = []

    def add_account(self, account): 
        self.accounts.append(account)

    def __str__(self):
        return f"Name = {self.name}, Number of accounts = {len(self.accounts)}"
    