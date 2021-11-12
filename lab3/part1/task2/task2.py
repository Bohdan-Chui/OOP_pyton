from Order import Order
from Customer import Customer
from PizzaManager import PizzaManager

def main():
    customer = Customer("Bohdan")
    Order(customer, PizzaManager.get_pizza_of_day()).order_pizza()
main()