class Customer:

    def __init__(self, name="Bohdan", surname="Chuy", patronymic="Serhiovich", mobile="380633129708"):
        try:
            self.set_name(name)
            self.set_surname(surname)
            self.set_patronymic(patronymic)
            self.set_mobile(mobile)
        except Exception as ve:
            print(ve)

    def set_name(self, name):
        if isinstance(name, str):
            self.__name = name
        else:
            raise TypeError("name must be a string")

    def set_surname(self, surname):
        if isinstance(surname, str):
            self.__surname = surname
        else:
            raise TypeError("surname must be a string")

    def set_patronymic(self, patronymic):
        if isinstance(patronymic, str):
            self.__patronymic = patronymic
        else:
            raise TypeError("patronymic must be a string")

    def set_mobile(self, mobile):
        if self.validNumber(mobile):
            self.__mobile = mobile
        else:
            raise TypeError("not valide mobile number")

    def validNumber(self, phone_number):
        if len(phone_number) != 12:
            return False
        for i in phone_number:
            int(i)
            if i in [0, 10]:
                if not phone_number[i].isalnum():
                    return False
        return True

    def get_name(self):
        return self.__name

    def get_surname(self):
        return self.__surname

    def get_patronymic(self):
        return self.__patronymic

    def get_mobile(self):
        return self.__mobile
