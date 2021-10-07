class Store:
    def __init__(self, price=0.0, description = '', dimenshion = 0):
        try:
            self.set_price(price)
            self.set_description(description)
            self.set_dimenshoin(dimenshion)
        except Exception as ve:
            print(ve)

    def set_price(self, price):
        if isinstance(price, float) or  isinstance(price, int):
            self.__price = price
        else:
            raise TypeError("price must be digit")

    def set_description(self, description):
        if isinstance(description, str):
            self.__descriprion = description
        else:
            raise TypeError("description must be a string")

    def set_dimenshoin(self, dimenshion):
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


# if __name__ == '__main__':
#     try:
#         phone = Store(10,"Phone", 12)
#         print(phone.store_to_str())
#
#         tablet = Store(14, "Tablet", 15)
#         print(tablet.store_to_str())
#
#         store = Store("loh", "Phone", 12)
#         print(store.store_to_str())
#
#     except Exception as ev:
#         print(ev)