from datetime import date


class Event:
    def __init__(self, name, date_event, regular_price):
        self.name = name
        self.date_event = date_event
        self.regular_price = regular_price

    @property
    def name(self):
        return self.__name

    @property
    def date_event(self):
        return self.__date_event

    @property
    def regular_price(self):
        return self.__regular_price

    @name.setter
    def name(self,name):
        if not isinstance(name, str):
            raise TypeError('name isn`t str type')
        self.__name = name

    @date_event.setter
    def date_event(self, date_event):
        if not isinstance(date_event, date):
            raise TypeError("date_event is not date type")
        self.__date_event = date_event

    @regular_price.setter
    def regular_price(self, regular_price):
        if not isinstance(regular_price, (int, float)):
            raise TypeError('price must be int of float')
        self.__regular_price = regular_price

    def __str__(self):
        return f'Event:\n' \
               f' name: {self.name}\n' \
               f' time: {self.date_event}\n' \
               f' regular price: {self.regular_price}'