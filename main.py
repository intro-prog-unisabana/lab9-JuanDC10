from utils import person_data, balance_summary
from bank_account import BankAccount
from person import Person

def main():
    persons = []

    while True:
        print("Choose an option:")
        print("1. Add a new person")
        print("2. Add an account to a person")
        print("3. Show all balances")
        print("4. Quit")

        choice = input()

        if choice == "1":
            person = person_data()
            persons.append(person)

        elif choice == "2":
            name = input("Enter the person's name:\n")

            found = None
            for p in persons:
                if p.name == name:
                    found = p
                    break

            if found:
                account_number = int(input("Enter a 4-digit account number:\n"))
                balance = float(input("Enter the initial balance:\n"))

                account = BankAccount(account_number, balance)
                found.add_account(account)
            else:
                print("Person not found.")

        elif choice == "3":
            if not persons:
                print("No data to show.")
            else:
                balance_summary(persons)

        elif choice == "4":
            print("Goodbye!")
            break

        else:
            print("Invalid option.")

if __name__ == "__main__":
    main()