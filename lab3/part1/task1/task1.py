from datetime import date


class RegularTicket:

    def __init__(self, price ,visitor, number, buy_date, event_data) :
        self.price = price
        self.visitor = visitor
        self.number = number
        self.buy_date = buy_date
        self.event_date = event_data

    @property
    def visitor(self):
        return self.__visitor

    @visitor.setter
    def visitor(self, visitor):
        if not isinstance(visitor, str):
            raise TypeError("visitor not a str")
        if not( visitor and visitor.strip()):
            raise TypeError("visitor empty")
        self.__visitor = visitor

    @property
    def buy_date(self):
        return self.__buy_date

    @buy_date.setter
    def buy_date(self, buy_date):
        if not isinstance(buy_date, date):
            raise TypeError("buyDate is not datetime type")
        self.__buy_date = buy_date

    @property
    def number(self):
        return self.__number

    @number.setter
    def number(self, number):
        if not isinstance(number, int):
            raise TypeError("number is not int type ")
        self.__number = number

    @property
    def price(self):
        return self.__price

    @price.setter
    def price(self, price):
        if not isinstance(price, int):
            raise TypeError("price is not int type ")
        self.__price = price


    @property
    def event_date(self):
        return self.__event_date

    @event_date.setter
    def event_date(self, event_data):
        if not isinstance(event_data, date):
            raise TypeError("event_data is not datetime type")
        self.__event_data = event_data


