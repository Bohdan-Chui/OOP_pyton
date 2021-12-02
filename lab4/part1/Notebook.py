
from datetime import datetime

import mysql
from mysql.connector import connect, Error

from lab4.part1.DatabaseConfig import host, user, password, dataBaseName
from lab4.part1.Person import Person


class Notebook:

    def __init__(self) :
        self.__connection = Notebook.connect()

    @staticmethod
    def connect():
        connector = mysql.connector.connect(
            host=host,
            user=user,
            password=password,
            database=dataBaseName,
        )
        return connector

    def __add__(self, person):
        if not isinstance(person, Person):
            raise TypeError("isn`t person type")
        print(person)
        insert_query =  f'INSERT INTO user (name, surname, number, birthday) VALUES(%s,%s,%s,%s)'
        with self.__connection.cursor() as cursor:
            cursor.execute(insert_query,(person.name, person.surname, person.mobile, person.birthday))
            self.__connection.commit()

    def __sub__(self, name):
        if not isinstance(name, str):
            raise TypeError("isn`t person type")
        print("delete " + name)
        delete_query = f"DELETE FROM user WHERE name = '%s' " % (name)
        with self.__connection.cursor() as cursor:
            cursor.execute(delete_query)
            self.__connection.commit()

    def __mul__(self, name):
        if not isinstance(name, str):
            raise TypeError("isn`t person type")
        print("delete " + name)
        select_query = f"SELECT name, surname, number, birthday  FROM user WHERE name = '%s' " % (name)
        with self.__connection.cursor() as cursor:
            cursor.execute(select_query)
            for reviewer in cursor.fetchall():
                return Person(reviewer[0],reviewer[1], reviewer[2], datetime.strptime(reviewer[3], '%Y-%m-%d').date())


