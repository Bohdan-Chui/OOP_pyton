import mysql
from mysql.connector import connect

host = "localhost"
user = "root"
password = "root"
dataBaseName = "python"


class Connector:

    def __init__(self):
        self.__connection = Connector.connect()

    @staticmethod
    def connect():
        connector = mysql.connector.connect(
            host=host,
            user=user,
            password=password,
            database=dataBaseName,
        )
        return connector
