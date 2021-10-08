class Store:

    def __init__(self, price = 0.0, description = ' ', dimenshion = 0.0):
            self.price = price
            self.descriprion = description
            self.dimenshion = dimenshion

    @property
    def price(self):
        return self.__price

    @price.setter
    def price(self, price):
        if isinstance(price, float) or  isinstance(price, int):
            self.__price = price
        else:
            raise TypeError("price must be digit")

    @property
    def description(self):
        return self.__description


    @description.setter
    def descriprion(self, description = 'default description'):
        if not isinstance(description, str):
            raise TypeError("description must be a string")
        if description and description.strip():
            self.__descriprion = description
        else:
            raise TypeError("description is empty")

    @property
    def dimenshion(self):
        return self.__dimenshion

    @dimenshion.setter
    def dimenshion(self, dimenshion = 0):
        if isinstance(dimenshion, float) or  isinstance(dimenshion, int):
            self.__dimenshion = dimenshion
        else:
            raise TypeError("dimenshion must be digit")

    def get_price(self):
        return self.__price

    def get_description(self):
        return self.__descriprion

    def get_dimension(self):
        return self.__dimenshion

    def __str__(self) -> str:
        return "descriprion: " + self.__descriprion + " \nprice: " + str(self.__price) + " \ndimenshion: " + str(self.__dimenshion)