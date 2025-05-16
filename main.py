from Tracker.tracker import Tracker

def load_main():  
    print("💰 Welcome to Finance Tracker 💰", end="\n")
    print("--------------------------------")

    tracker = Tracker()
    is_active = True

    while is_active:
        print("\nWhat do you want to do?")
        print("1. Add a transaction")
        print("2. View financial report")
        print("3. View balance")
        print("4. Exit")

        input_option = input("Please select an option : 1, 2, 3 or 4\n").strip()

        match input_option:
            case "1":
                # here code for adding a transaction
                tracker.add_transaction()
            case "2":
                # here code for financial report
                tracker.view_report()
            case "3":
                # check balance
                print(f"Current balance : $ {tracker.balance}")
            case "4":
                print("Thank you for using Finance Tracker. Goodbye!")
                print("---------------------------------------------")
                is_active = False
            case _:
                print("❌ Invalid choice. Please select an option: 1, 2 or 3\n")    

## Calling the main function
load_main() 

