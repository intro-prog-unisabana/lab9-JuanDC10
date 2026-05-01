# utils.py
from bank_account import BankAccount
from person import Person

def person_data(): 
    name = input("Enter the person's name:\n")
    person = Person(name)

    while True: 
        account_number = int(input("Enter a 4-digit account number:\n"))
        balance = float(input("Enter the initial balance:\n"))

        account = BankAccount(account_number, balance)
        person.add_account(account)

        done = input("Are you done adding accounts? (yes/no):\n")
        if done == "yes":
            break
    return person
