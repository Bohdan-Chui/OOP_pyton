from datetime import date


class RegularTicket:

    def __init__(self, number, visitor, event_date, event_price):
        self.type = 'regular'
        self.visitor = visitor
        self.number = number
        self.event_date = event_date
        self.price = event_price

    @property
    def type(self):
        return self.__type

    @type.setter
    def type(self, type):
        self.__type = type

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
    def number(self):
        return self.__number

    @number.setter
    def number(self, number):
        if not isinstance(number, int):
            raise TypeError("number is not int type ")
        self.__number = number

    @property
    def event_date(self):
        return self.__event_date

    @event_date.setter
    def event_date(self, event_date):
        if not isinstance(event_date, date):
            raise TypeError("event_date is not date type ")
        self.__event_date = event_date

    @property
    def price(self):
        return self.__price

    @price.setter
    def price(self, event_price):
        if not isinstance(event_price, (int, float)):
            raise TypeError("event_price is not int or float type ")
        self.__price = event_price

    def __str__(self):
        return f'Regular ticket\n number: {self.number}\n' \
               f' visitor: {self.visitor}\n price: {self.price}\n' \
               f' event date {self.event_date}'

class AdvanceTicket(RegularTicket):

    def __init__(self, number, visitor, event_date, event_price):
        super().__init__(number, visitor, event_date, event_price)
        self.price = event_price
        self.type = 'advance'

    @property
    def price(self):
        return self.__price

    @price.setter
    def price(self, price):
        if not isinstance(price, (int, float)):
            raise TypeError("price is not int or float type ")
        self.__price = price * 0.6

    def __str__(self):
        return f'Advance ticket\n number: {self.number}\n' \
               f' visitor: {self.visitor}\n price: {self.price}\n' \
               f' event date {self.event_date}'


class LateTicket(RegularTicket):

    def __init__(self,number, visitor, event_date, event_price):
        super().__init__(number, visitor, event_date, event_price)
        self.price = event_price
        self.type = 'late'

    @property
    def price(self):
        return self.__price

    @price.setter
    def price(self, price):
        if not isinstance(price, (int, float)):
            raise TypeError("price is not int or float type ")
        self.__price = price * 1.1

    def __str__(self):
        return f'Late ticket\n number: {self.number}\n' \
               f' visitor: {self.visitor}\n price: {self.price}\n' \
               f' event date {self.event_date}'


class StudentTicket(RegularTicket):

    def __init__(self,number, visitor, event_date, event_price):
        super().__init__(number, visitor, event_date, event_price)
        self.price = event_price
        self.type = 'student'

    @property
    def price(self):
        return self.__price

    @price.setter
    def price(self, price):
        if not isinstance(price, (int, float)):
            raise TypeError("price is not int or float type ")
        self.__price = price * 0.5

    def __str__(self):
        return f'Student ticket\n number: {self.number}\n' \
               f' visitor: {self.visitor}\n price: {self.price}\n' \
               f' event date {self.event_date}'


