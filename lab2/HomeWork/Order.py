from Store import Store
from Customer import Customer

"""
    Class contain data about the customer who carried it out and products. 
    Implement a method for calculating the total order value.
"""


class Order:

    def __init__(self, user, *args):
        self.user = user
        self.products = args

    @property
    def user(self):
        return self.__user

    @user.setter
    def user(self, user):
        if isinstance(user, Customer):
            self.__user = user
        else:
            raise TypeError('User must be Customer type')

    @property
    def products(self):
        return self.__products

    @products.setter
    def products(self, products):
        if any(not isinstance(product, Store) for product in products):
            raise TypeError("Products must be of Product type")
        self.__products = list(products)

    def add_product(self, product):
        if isinstance(product, Store):
            self.__products.append(product)
        else:
            raise TypeError('Product must be Store type')

    def dell_product(self, product):
        self.products.remove(product)

    def total_order_value(self):
        total = 0
        for price in self.__products:
            total += price.get_price()
        return total
