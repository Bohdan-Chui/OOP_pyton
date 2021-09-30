from math import gcd


class Rational:
    def __init__(self, numerator = 0, denumerator = 1):
        if  not isinstance(denumerator, int):
            raise TypeError("illegal type denumerator")
        if  not isinstance(numerator, int):
            raise TypeError("illegal type numerator")
        if denumerator == 0:
            raise ZeroDivisionError("denumerator == 0")

        divisor = gcd(numerator,denumerator)
        self.__numerator = int(numerator / divisor)
        self.__denumerator = int(denumerator / divisor)

    def to_str(self) -> str:
        return str(self.__numerator) + "/" + str(self.__denumerator)

    def to_float_format(self) -> float:
        return float(self.__numerator), float(self.__denumerator)


if __name__ == '__main__':
    try:
        rational = Rational(2,4)
        print(rational.to_str())
        print(rational.to_float_format())
    except Exception as ve:
        print(ve)


