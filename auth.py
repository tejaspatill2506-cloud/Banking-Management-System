from database import Database


class Authentication:

    def __init__(self):
        self.db = Database()

    def login(self):

        print("\n========== Login ==========")

        account_no = input("Enter Account Number : ")

        password = input("Enter Password : ")

        query = """
        SELECT * FROM customers
        WHERE account_no=%s AND password=%s
        """

        result = self.db.fetchone(query, (account_no, password))

        if result:

            print("\nLogin Successful!")

            return result[0]

        else:

            print("\nInvalid Account Number or Password.")

            return None