from Customer import Customer
from Pizzas import *

class Order:
    ingredients = {'mozzarella': 20,
                   'ham': 40,
                   'bacon': 30,
                   'BBQ sauce': 10,
                   'tomato': 15}

    def __init__(self, customer, pizza):
        self.customer = customer
        self.pizza = pizza

    @property
    def customer(self):
        return self.__customer

    @customer.setter
    def customer(self, customer):
        if not isinstance(customer, Customer):
            raise TypeError("not Customer type")
        self.__customer = customer

    @property
    def pizza(self):
        return self.__pizza

    @pizza.setter
    def pizza(self, pizza):
        if not isinstance(pizza, Pizza):
            raise TypeError('isn`t Pizza type')
        self.__pizza = pizza

    def order_pizza(self):
        print('Hello, my customer\n today pizza is: \n' + str(self.pizza))
        if input(f"Would you like something to add Y/N ?").lower() == "y":
            print(self.ingredients)
            for item in self.ingredients:
                if input(f"Would you like to add {item} Y/N ?").lower() == "y":
                    self.pizza.ingredients.append(item)
                    self.pizza.price += self.ingredients[item]
        print('You pizza:' + str(self.pizza))

