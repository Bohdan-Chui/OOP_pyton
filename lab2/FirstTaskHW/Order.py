from Customer import Customer
from Store import Store


class Order:

    def __init__(self, user, *args):
        self.__user = user
        self.__products = args

    def print_orders(self):
        for i in self.__products:
            print (i)

    def total_order_value(self):
        total = 0
        for price in self.__products:
            total += price.get_price()
        return total

# if __name__ == '__main__':
#     try:
#         order = Order(Customer(),Store(12.3,"Phone", 12), Store(12.3,"Phone", 12), Store(12.3,"Phone", 12))
#         print(order.total_order_value())
#     except Exception as ve:
#         print(ve)