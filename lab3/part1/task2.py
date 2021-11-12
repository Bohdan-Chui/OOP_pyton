import datetime
import json


class Pizza:
    def __init__(self, day, name, price, ingredients):
        self.day = day
        self.name = name
        self.price = price
        self.ingredients = ingredients

    @property
    def day(self):
        return self.__day

    @day.setter
    def day(self, day):
        if not isinstance(day, str):
            raise TypeError("day must be str")
        self.__day = day

    @property
    def name(self):
        return self.__name

    @property
    def price(self):
        return self.__price

    @property
    def ingredients(self):
        return self.__ingredients

    @price.setter
    def price(self, price):
        if not isinstance(price, int):
            raise TypeError("price must be int")
        self.__price = price

    @name.setter
    def name(self, name):
        if not isinstance(name, str):
            raise TypeError("name must be str")
        self.__name = name

    @ingredients.setter
    def ingredients(self, value):
        if any(not isinstance(ingretients, str) for ingretients in value):
            raise TypeError("ingredients must be str")
        self.__ingredients = value

    def __str__(self):
        return f"{self.name}\n price: " \
               f"{self.price}\n ingretients {self.ingredients}\n "

    def encoder(self):
        return {"day": self.day,
                "name": self.name,
                "price": self.price,
                "ingredients": self.ingredients}


class MondayPizza(Pizza):

    def __init__(self, name, price, ingredients):
        super().__init__("Monday", name, price, ingredients)

    def __str__(self):
        return f"Monday pizza:  {self.name}\n price: " \
               f"{self.price}\n ingredients {self.ingretients}\n "


class TuesdayPizza(Pizza):

    def __init__(self, name, price, ingredients):
        super().__init__("Tuesday", name, price, ingredients)

    def __str__(self):
        return f"Tuesday pizza:  {self.name}\n price: " \
               f"{self.price}\n ingredients {self.ingretients}\n "


class WednesdayPizza(Pizza):

    def __init__(self, name, price, ingredients):
        super().__init__("Wednesday", name, price, ingredients)

    def __str__(self):
        return f"Wednesday pizza:  {self.name}\n price: " \
               f"{self.price}\n ingredients {self.ingretients}\n "


class ThursdayPizza(Pizza):

    def __init__(self, name, price, ingredients):
        super().__init__("Thursday", name, price, ingredients)

    def __str__(self):
        return f"Thursday pizza:  {self.name}\n price:" \
               f" {self.price}\n ingretients {self.ingretients}\n "


class FridayPizza(Pizza):

    def __init__(self, name, price, ingredients):
        super().__init__("Friday", name, price, ingredients)


class SaturdayPizza(Pizza):

    def __init__(self, name, price, ingredients):
        super().__init__("Saturday", name, price, ingredients)

    def __str__(self):
        return f"Saturday pizza:  {self.name}\n price: " \
               f"{self.price}\n ingretients {self.ingretients}\n "


class SundayPizza(Pizza):

    def __init__(self, name, price, ingredients):
        super().__init__("Sunday", name, price, ingredients)

    def __str__(self):
        return f"Sunday pizza:  {self.name}\n price: " \
               f"{self.price}\n ingretients {self.ingretients}\n "


class PizzaManager:

    @staticmethod
    def serialize():
        s = [MondayPizza("4cheeses", 12, ["Cheese", "rogfort"]),
             TuesdayPizza("Americano", 12, ["sausage", "bbq souse"]),
             WednesdayPizza("Margarita", 12, ["tomats", "basilica"]),
             ThursdayPizza("Diablo", 12, ["prosciutto", "beacon"]),
             FridayPizza("Pepperoni", 12, ["rogfort", "sausage"]), SaturdayPizza("Bavarian", 12, ["Cheese", "beacon"]),
             SundayPizza("Rancho", 12, ["meat", "tomates"])]

        data = {'pizza': []}
        for obj in s:
            data['pizza'].append(obj.encoder())

        with open('pizza.json', 'w') as outfile:
            json.dump(data, outfile, indent=4)

    @staticmethod
    def get_pizza_of_day():
        day = datetime.datetime.now().strftime("%A")
        with open('pizza.json') as json_file:
            data = json.load(json_file)
            for p in data['pizza']:
                if p['day'] == day:
                    return Pizza(day, p['name'], p['price'], p['ingredients'])


class Customer:
    def __init__(self, name):
        self.name = name

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name):
        if not isinstance(name, str):
            TypeError("name must be str")
        if name and name.strip():
            self.__name = name
        else:
            raise TypeError("name customer is empty")


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




def main():
    customer = Customer("Bohdan")
    Order(customer, PizzaManager.get_pizza_of_day()).order_pizza()
main()