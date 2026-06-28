import mysql.connector
from config import HOST, USER, PASSWORD, DATABASE


class Database:

    def __init__(self):

        self.connection = mysql.connector.connect(

            host="localhost",
            user="root",
            password="tejaspatil@2004",
            database="bankinfo"

        )

        self.cursor = self.connection.cursor()

    def execute(self, query, values=None):

        if values:
            self.cursor.execute(query, values)
        else:
            self.cursor.execute(query)

        self.connection.commit()

    def fetchone(self, query, values=None):

        if values:
            self.cursor.execute(query, values)
        else:
            self.cursor.execute(query)

        return self.cursor.fetchone()

    def fetchall(self, query, values=None):

        if values:
            self.cursor.execute(query, values)
        else:
            self.cursor.execute(query)

        return self.cursor.fetchall()

    def close(self):

        self.cursor.close()
        self.connection.close()