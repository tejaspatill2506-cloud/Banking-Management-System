# deposit()

# withdraw()

# transfer()

# save_transaction()

# mini_statement()

# transaction_history()


from database import Database
from logger import Logger


class Transaction:

    def __init__(self):

        self.db = Database()

    # Deposit

    def deposit(self, account_no):

        amount = float(input("Enter Amount : "))

        query = """
        UPDATE customers
        SET balance = balance + %s
        WHERE account_no=%s
        """

        self.db.execute(query, (amount, account_no))

        self.db.execute(

            """
            INSERT INTO transactions
            (account_no,transaction_type,amount,balance_after)
            VALUES
            (%s,'Deposit',%s,
            (SELECT balance FROM customers WHERE account_no=%s))
            """,

            (account_no, amount, account_no)

        )

        Logger.write(
            f"Account {account_no} Deposited ₹{amount}"
        )

        print("Deposit Successful.")

    # Withdraw

    def withdraw(self, account_no):

        amount = float(input("Enter Amount : "))

        balance = self.db.fetchone(

            "SELECT balance FROM customers WHERE account_no=%s",

            (account_no,)

        )[0]

        if amount > balance:

            print("Insufficient Balance")

            return

        self.db.execute(

            """
            UPDATE customers
            SET balance=balance-%s
            WHERE account_no=%s
            """,

            (amount, account_no)

        )

        self.db.execute(

            """
            INSERT INTO transactions
            (account_no,transaction_type,amount,balance_after)
            VALUES
            (%s,'Withdraw',%s,
            (SELECT balance FROM customers WHERE account_no=%s))
            """,

            (account_no, amount, account_no)

        )

        Logger.write(
            f"Account {account_no} Withdraw ₹{amount}"
        )

        print("Withdraw Successful.")

    # Balance

    def balance(self, account_no):

        balance = self.db.fetchone(

            "SELECT balance FROM customers WHERE account_no=%s",

            (account_no,)

        )

        print("\nCurrent Balance : ₹", balance[0])

    # Mini Statement

    def mini_statement(self, account_no):

        print("\n===== Mini Statement =====")

        records = self.db.fetchall(

            """
            SELECT transaction_type,
            amount,
            balance_after,
            transaction_date
            FROM transactions
            WHERE account_no=%s
            ORDER BY transaction_date DESC
            LIMIT 5
            """,

            (account_no,)

        )

        for row in records:

            print("--------------------------------------")

            print("Type    :", row[0])

            print("Amount  :", row[1])

            print("Balance :", row[2])

            print("Date    :", row[3])

    # Full Transaction History

    def transaction_history(self, account_no):

        print("\n===== Transaction History =====")

        records = self.db.fetchall(

            """
            SELECT transaction_id,
            transaction_type,
            amount,
            balance_after,
            transaction_date

            FROM transactions

            WHERE account_no=%s

            ORDER BY transaction_date DESC
            """,

            (account_no,)

        )

        for row in records:

            print("---------------------------------------")

            print("Transaction ID :", row[0])

            print("Type           :", row[1])

            print("Amount         :", row[2])

            print("Balance        :", row[3])

            print("Date           :", row[4])