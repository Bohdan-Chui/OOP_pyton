class Rectangle:

    def __init__(self, lenght, hight):
        self.set_lenght(lenght)
        self.set_hight(hight)

    def set_lenght(self, lenght = 1.0):
            if isinstance(lenght, float):
                if  0 < lenght < 20:
                    self.__lenght = lenght
                else:
                    raise ValueError("illegal argument lenght")
            else:
                raise TypeError("illegal type lenght")

    def set_hight(self, hight = 1.0):
        if isinstance(hight, float):
            if 0 < hight < 20:
                self.__hight = hight
            else:
                raise ValueError("illegal argument lenght")
        else:
            raise TypeError("illegal type lenght")

    def get_hight(self):
        return  self.__hight

    def get_lenght(self):
        return  self.__lenght

    def perimetr_area(self):
        return self.__lenght * self.__hight, (self.__hight+self.__lenght)*2


if __name__ == '__main__':
    try:
        rectangle = Rectangle()
        rectangle.set_hight(10.0)
        rectangle.set_lenght(14.0)
        print(rectangle.perimetr_area())
    except Exception as ve:
        print(ve)