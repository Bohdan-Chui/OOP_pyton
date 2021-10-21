"""
    class contains background information of product prices (product code, price of 1 product)
"""


class Product:
    def __init__(self, code, price):
        self.code = code
        self.price = price

    @property
    def code(self):
        return self.__code

    @property
    def price(self):
        return self.__price

    @code.setter
    def code(self, code):
        if not isinstance(code, int):
            raise TypeError('code must be int')
        self.__code = code

    @price.setter
    def price(self, price):
        if not isinstance(price,(int,float)):
            raise TypeError('price must be int or float')
        self.__price = price

    def __str__(self) -> str:
        return f'code->{self.__code} price:{self.__price}'

