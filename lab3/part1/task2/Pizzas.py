
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
               f"{self.price}\n ingredients {self.ingredients}\n "

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
               f" {self.price}\n ingredients {self.ingretients}\n "


class FridayPizza(Pizza):

    def __init__(self, name, price, ingredients):
        super().__init__("Friday", name, price, ingredients)

    def __str__(self):
        return f"Friday pizza:  {self.name}\n price: " \
               f"{self.price}\n ingredients {self.ingretients}\n "


class SaturdayPizza(Pizza):

    def __init__(self, name, price, ingredients):
        super().__init__("Saturday", name, price, ingredients)

    def __str__(self):
        return f"Saturday pizza:  {self.name}\n price: " \
               f"{self.price}\n ingredients {self.ingretients}\n "


class SundayPizza(Pizza):

    def __init__(self, name, price, ingredients):
        super().__init__("Sunday", name, price, ingredients)

    def __str__(self):
        return f"Sunday pizza:  {self.name}\n price: " \
               f"{self.price}\n ingredients {self.ingretients}\n "


