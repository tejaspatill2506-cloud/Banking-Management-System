class Account:

    def __init__(self,
                 account_no,
                 name,
                 email,
                 mobile,
                 password,
                 balance):

        self.account_no = account_no
        self.name = name
        self.email = email
        self.mobile = mobile
        self.password = password
        self.balance = balance

    def display(self):

        print("\n==============================")

        print("Account Number :", self.account_no)

        print("Name           :", self.name)

        print("Email          :", self.email)

        print("Mobile         :", self.mobile)

        print("Balance        : ₹", self.balance)

        print("==============================")