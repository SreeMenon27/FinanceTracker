# Module that contains all modules related to adding, deleting transactions
import time
import json
import os
from Tracker.config import INCOME_CATEGORIES, EXPENSE_CATEGORIES, INITIAL_BALANCE

class Tracker:
    BASE_DIR = os.path.dirname(os.path.abspath(__file__))  # path to /Tracker
    filepath = os.path.normpath(os.path.join(BASE_DIR, '..', 'Data', 'records.json'))

    def __init__(self):
        self.transaction_type = ""
        self.transaction_category = ""
        self.amount = 0.0
        self._load_transactions()

    def __len__(self):
        return len(self.transactions)

    def __str__(self):
        return f"Finance Tracker | Current Balance: ${self.balance:.2f} | Transactions: {len(self.transactions)}"

    @property
    def balance(self):
        total = 0
        if not self.transactions:
            return INITIAL_BALANCE
        
        for item in self.transactions:
            amt = float(item.get("amount",0))
            if item.get("transaction_type") == "income":
                total +=amt
            else:
                total -=amt
        return total


    def _get_income_category(self):
        # Retrieve all income categories
        print("--------------------------------")
        print("\n Choose category:")
        categories = INCOME_CATEGORIES
        
        for keys,val in categories.items(): 
            print(f"{keys}. {val}")

        while True:
            selected_category = input("Select a category : \n").strip()
            if selected_category in categories:
                return categories[selected_category]
            else:
                print("❌ Invalid choice. Please select a valid number from the list.")            

        
    def _get_expense_category(self):
        # Retrieve all expense categories
        print("--------------------------------")
        print("\nChoose category:")
        expense_category = EXPENSE_CATEGORIES

        for key,val in expense_category.items():    
            print(f"{key}. {val}")

        while True:
            selected_category = input("Select a category : \n").strip()
            if selected_category in expense_category:
                return expense_category[selected_category]
            else:
                print("❌ Invalid choice. Please select a valid number from the list.") 
            

    def add_transaction(self):
        record = {}
        ## Transaction type, transaction category, amount, timestamp
        print("--------------------------------")
        print("\nWhat do you want to add?")
        print("1. Income")
        print("2. Expense")
        while True:
            transaction_choice = input("Select an option : 1 or 2\n").strip()
            if transaction_choice == "1":
                self.transaction_type = "income"
                self.transaction_category = self._get_income_category()
                break
            elif transaction_choice == "2":
                self.transaction_type = "expense"
                self.transaction_category= self._get_expense_category()        
                break        
            else:
                print("❌ Invalid choice. Select an option: 1 or 2\n")

        while True:
            try:
                amount = float(input("Enter the amount $: ").strip())
                self.amount = amount
                break
            except ValueError:
                print("❌ Invalid amount. Please enter a numeric value.")
                
       
        self.timestamp = time.strftime("%Y-%m-%d %H:%M:%S")

        record = {
            "transaction_type" : self.transaction_type,
            "transaction_category" : self.transaction_category,
            "amount" : self.amount,
            "timestamp" : self.timestamp
        }
        self.transactions.append(record)

        print(f"\n✅ Transaction added! New balance: ${self.balance:.2f}")
        self._save_transactions()


    def _save_transactions(self):
        ## Write to JSON file
        try:

            print(f"Saving transaction to {Tracker.filepath}")

            with open(Tracker.filepath,"w+") as f:
                json.dump(self.transactions, f, indent=4)

            print("✅ Transactions saved successfully.")

        except FileNotFoundError:
            print("❌ File path not found.")
        except Exception as e:
            print(f"❌ An error occurred while saving transactions: {e}")


    def _load_transactions(self):
        # Load existing transactions from the JSON file and update balance.
        try:
            if os.path.exists(self.filepath) and os.path.getsize(self.filepath) > 0:
                with open(self.filepath,"r") as f:
                    data = json.load(f)
                    self.transactions = data
                    print(f"Your current balance: $ {self.balance} ")
                    print("________________________________")
            else:
                self.transactions = []

        except json.JSONDecodeError:
            print("❌ Error: records.json contains invalid JSON.")


    def view_report(self):
        if self.transactions:
            print("-" * 70)
            print(f"{'No.':<4} {'Type':<10} {'Category':<18} {'Amount':<10} {'Timestamp'}")
            print("-" * 70)
            for i, item in enumerate(self.transactions, start=1):
                print(f"{i:<4} {item.get('transaction_type', ''):<10} {item.get('transaction_category', ''):<18} "
                    f"{item.get('amount', 0):<10.2f} {item.get('timestamp', '')}")
            print("-" * 70)
            # "Balance" under Type, balance value under Amount
            print(f"{'':<4} {'Balance':<10} {'':<18} {self.balance:<10.2f}")
            print("-" * 70)
        else:
            print("-----  No transactions to display  -----")



