from database import Database
from account import Account
from transaction import Transaction
from logger import Logger


class Bank:

    def __init__(self):

        self.db = Database()
        self.transaction = Transaction()

    # -------------------------------
    # Create Account
    # -------------------------------

    def create_account(self):

        print("\n===== Create Account =====")

        name = input("Enter Name : ")
        email = input("Enter Email : ")
        mobile = input("Enter Mobile : ")
        password = input("Create Password : ")

        try:

            balance = float(input("Enter Initial Deposit : "))

            if balance < 0:
                print("Balance cannot be negative.")
                return

            query = """
            INSERT INTO customers
            (name,email,mobile,password,balance)
            VALUES(%s,%s,%s,%s,%s)
            """

            self.db.execute(
                query,
                (name, email, mobile, password, balance)
            )

            account = self.db.fetchone(
                "SELECT MAX(account_no) FROM customers"
            )[0]

            self.db.execute(
                """
                INSERT INTO transactions
                (account_no,transaction_type,amount,balance_after)
                VALUES(%s,'Deposit',%s,%s)
                """,
                (account, balance, balance)
            )

            Logger.write(
                f"New Account Created : {account}"
            )

            print("\nAccount Created Successfully")
            print("Your Account Number :", account)

        except Exception as e:

            print("Error :", e)

    # -------------------------------
    # Search Account
    # -------------------------------

    def search_account(self):

        account = input("Enter Account Number : ")

        data = self.db.fetchone(
            "SELECT * FROM customers WHERE account_no=%s",
            (account,)
        )

        if data:

            obj = Account(*data)

            obj.display()

        else:

            print("Account Not Found.")

    # -------------------------------
    # Display All Accounts
    # -------------------------------

    def display_accounts(self):

        records = self.db.fetchall(
            "SELECT * FROM customers"
        )

        print("\n========== Customer List ==========")

        for row in records:

            obj = Account(*row)

            obj.display()

    # -------------------------------
    # Update Account
    # -------------------------------

    def update_account(self):

        account = input("Enter Account Number : ")

        data = self.db.fetchone(

            "SELECT * FROM customers WHERE account_no=%s",

            (account,)

        )

        if not data:

            print("Account Not Found.")

            return

        print("\nLeave blank to keep old value.\n")

        name = input(f"Name ({data[1]}) : ")

        email = input(f"Email ({data[2]}) : ")

        mobile = input(f"Mobile ({data[3]}) : ")

        if name == "":
            name = data[1]

        if email == "":
            email = data[2]

        if mobile == "":
            mobile = data[3]

        self.db.execute(

            """
            UPDATE customers
            SET name=%s,
                email=%s,
                mobile=%s
            WHERE account_no=%s
            """,

            (name, email, mobile, account)

        )

        Logger.write(

            f"Account Updated : {account}"

        )

        print("Account Updated Successfully.")

    # -------------------------------
    # Delete Account
    # -------------------------------

    def delete_account(self):

        account = input("Enter Account Number : ")

        data = self.db.fetchone(

            "SELECT * FROM customers WHERE account_no=%s",

            (account,)

        )

        if not data:

            print("Account Not Found.")

            return

        self.db.execute(

            "DELETE FROM transactions WHERE account_no=%s",

            (account,)

        )

        self.db.execute(

            "DELETE FROM customers WHERE account_no=%s",

            (account,)

        )

        Logger.write(

            f"Account Deleted : {account}"

        )

        print("Account Deleted Successfully.")

    # -------------------------------
    # Deposit
    # -------------------------------

    def deposit(self, account):

        self.transaction.deposit(account)

    # -------------------------------
    # Withdraw
    # -------------------------------

    def withdraw(self, account):

        self.transaction.withdraw(account)

    # -------------------------------
    # Balance Enquiry
    # -------------------------------

    def balance(self, account):

        self.transaction.balance(account)

    # -------------------------------
    # Mini Statement
    # -------------------------------

    def mini_statement(self, account):

        self.transaction.mini_statement(account)

    # -------------------------------
    # Transaction History
    # -------------------------------

    def transaction_history(self, account):

        self.transaction.transaction_history(account)