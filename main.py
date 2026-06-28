from bank import Bank
from auth import Authentication

bank = Bank()
auth = Authentication()

logged_in_account = None

while True:

    print("\n====================================")
    print("      BANKING MANAGEMENT SYSTEM")
    print("====================================")

    print("1. Create Account")
    print("2. Login")
    print("3. Deposit")
    print("4. Withdraw")
    print("5. Balance Check")
    print("6. Mini Statement")
    print("7. Transaction History")
    print("8. Search Account")
    print("9. Display All Accounts")
    print("10. Update Account")
    print("11. Delete Account")
    print("12. Logout")
    print("13. Exit")

    choice = input("\nEnter Choice : ")

    try:

        if choice == "1":
            bank.create_account()

        elif choice == "2":

            account = auth.login()

            if account:
                logged_in_account = account

        elif choice == "3":

            if logged_in_account:
                bank.deposit(logged_in_account)
            else:
                print("Please Login First.")

        elif choice == "4":

            if logged_in_account:
                bank.withdraw(logged_in_account)
            else:
                print("Please Login First.")

        elif choice == "5":

            if logged_in_account:
                bank.balance(logged_in_account)
            else:
                print("Please Login First.")

        elif choice == "6":

            if logged_in_account:
                bank.mini_statement(logged_in_account)
            else:
                print("Please Login First.")

        elif choice == "7":

            if logged_in_account:
                bank.transaction_history(logged_in_account)
            else:
                print("Please Login First.")

        elif choice == "8":

            bank.search_account()

        elif choice == "9":

            bank.display_accounts()

        elif choice == "10":

            bank.update_account()

        elif choice == "11":

            bank.delete_account()

        elif choice == "12":

            logged_in_account = None

            print("Logout Successful.")

        elif choice == "13":

            print("\nThank You for using Banking Management System.")
            break

        else:

            print("Invalid Choice.")

    except Exception as e:

        print("Error :", e)