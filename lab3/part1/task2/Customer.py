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
