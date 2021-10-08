import re


class Customer:

    def __init__(self, name = 'Unknown', surname = 'Unknown', patronymic = 'Unknown', mobile = '+380(00)-000-00-00'):
            self.name = name
            self.surname = surname
            self.patronymic = patronymic
            self.mobile = mobile

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
    def patronymic(self):
        return self.__patronymic

    @patronymic.setter
    def patronymic(self, patronymic):
        if not isinstance(patronymic, str):
            raise TypeError("patronymic must be a string")
        if patronymic.strip():
            self.__patronymic = patronymic
        else:
            raise TypeError("patronymic is empty")

    @property
    def mobile(self):
        return self.mobile

    @mobile.setter
    def mobile(self, mobile):
        pattern = re.compile("^\\+[0-9]{3}\\((\\d{2})\\)-\\d{3}-\\d{2}-\\d{2}")
        if not pattern.match(mobile):
            raise ValueError
        self.__phone_number = mobile

    def get_name(self):
        return self.__name

    def get_surname(self):
        return self.__surname

    def get_patronymic(self):
        return self.__patronymic

    def get_mobile(self):
        return self.__mobile
