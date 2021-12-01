import math
from math import gcd


class Rational:
    def __init__(self, numerator=0, denumerator=1):
        if not isinstance(numerator, int):
            raise TypeError("illegal type numerator")
        if not isinstance(denumerator, int):
            raise TypeError("illegal type denumerator")
        if denumerator == 0:
            raise ZeroDivisionError("denumerator == 0")
        self.divisor = gcd(numerator, denumerator)
        self.numerator = numerator
        self.denumerator = denumerator

    @property
    def divisor(self):
        return self.__divisor

    @property
    def numerator(self):
        return self.__numerator

    @property
    def denumerator(self):
        return self.__denumerator

    @divisor.setter
    def divisor(self, divisor):
        if not isinstance(divisor, int):
            raise TypeError("illegal type divisor")
        self.__divisor = divisor

    @numerator.setter
    def numerator(self, numerator):
        if not isinstance(numerator, int):
            raise TypeError("illegal type numerator")
        self.__numerator = numerator // self.divisor

    @denumerator.setter
    def denumerator(self, denumerator):
        if not isinstance(denumerator, int):
            raise TypeError("illegal type denumerator")
        if denumerator == 0:
            raise ZeroDivisionError("denumerator == 0")
        self.__denumerator = denumerator // self.divisor

    def __str__(self):
        return str(self.__numerator) + "/" + str(self.__denumerator)

    def to_float_format(self) -> float:
        return self.__numerator / self.__denumerator

    def __eq__(self, other):
        if not isinstance(other,Rational):
            raise TypeError("not Rational type")
        if(self.numerator == other.numerator and self.denumerator == other.denumerator):
            return True
        else:
            return False

    def __mul__(self, other):
        if not isinstance(other,Rational):
            raise TypeError("not Rational type")
        return Rational(self.numerator * other.numerator, self.denumerator * other.denumerator)

    def __truediv__(self, other):
        if not isinstance(other,Rational):
            raise TypeError("not Rational type")
        return Rational(self.numerator * other.denumerator, self.denumerator * other.numerator)

    def __add__(self, other):
        if not isinstance(other,Rational):
            raise TypeError("not Rational type")
        lcd = abs(other.denumerator * self.denumerator) // math.gcd(other.denumerator, self.denumerator)
        return Rational(int(lcd/self.denumerator*self.numerator + lcd/other.denumerator*other.numerator), lcd)

    def __sub__(self, other):
        if not isinstance(other,Rational):
            raise TypeError("not Rational type")
        lcd = abs(other.denumerator * self.denumerator) // math.gcd(other.denumerator, self.denumerator)
        return Rational(int(lcd / self.denumerator - self.numerator + lcd/other.denumerator * other.numerator), lcd)

    def __floordiv__(self, other):
        if not isinstance(other,Rational):
            raise TypeError("not Rational type")
        rat = self.__truediv__(self,other)
        return Rational(rat.numerator // rat.numerator)

    def __isub__(self, other):
        return self.__sub__(other)

    def __iadd__(self, other):
        return self.__add__(other)

    def __imul__(self, other):
        return self.__mul__( other)

    def __idiv__(self, other):
        return self.__truediv__(other)

    def __ifloordiv__(self, other):
        return self.__floordiv__(other)

    def __ne__(self, other):
        return not self.__eq__(other)
