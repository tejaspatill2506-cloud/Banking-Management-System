from datetime import datetime


class Logger:

    @staticmethod
    def write(message):

        with open("bank.log", "a") as file:

            file.write(

                f"{datetime.now()} : {message}\n"

            )