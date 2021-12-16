import re
from datetime import date


class Person:

    def __init__(self, name='Unknown', surname='Unknown', mobile='+380(00)-000-00-00', birthday = date(1800, 1, 1)):
        self.name = name
        self.surname = surname
        self.mobile = mobile
        self.birthday = birthday

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name):
        if not isinstance(name, str):
            raise TypeError("name must be a string")
        if name and name.strip():
            self.__name = name
        else:
            raise TypeError("name customer is empty")

    @property
    def surname(self):
        return self.__surname

    @surname.setter
    def surname(self, surname):
        if not isinstance(surname, str):
            raise TypeError("surname must be a string")
        if surname and surname.strip():
            self.__surname = surname
        else:
            raise TypeError("surname is empty")

    @property
    def mobile(self):
        return self.__mobile

    @mobile.setter
    def mobile(self, mobile):
        pattern = re.compile("^\\+[0-9]{3}\\((\\d{2})\\)-\\d{3}-\\d{2}-\\d{2}")
        if not pattern.match(mobile):
            raise ValueError("not mobile matches")
        self.__mobile = mobile

    @property
    def birthday(self):
        return self.__birthday

    @birthday.setter
    def birthday(self, birthday):
        if not isinstance(birthday, date):
            raise TypeError("birthday is not date type")
        self.__birthday = birthday

    def __str__(self) -> str:
        return f'Person name {self.__name} surname {self.surname} mobile {self.mobile} date {self.birthday}'

