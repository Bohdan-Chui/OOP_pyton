from Pizzas import *
import datetime
import json


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
        with open('./task2/pizza.json') as json_file:
            data = json.load(json_file)
            for p in data['pizza']:
                if p['day'] == day:
                    return Pizza(day, p['name'], p['price'], p['ingredients'])
