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
        self.__numerator = numerator
        self.__denumerator = denumerator
        self.__store()

    @property
    def divisor(self):
        return self.__divisor

    @property
    def numerator(self):
        return self.__numerator

    @property
    def denumerator(self):
        return self.__denumerator

    def __store(self):
        divisor = gcd(self.numerator, self.denumerator)
        self.__denumerator = self.denumerator // divisor
        self.__numerator = self.numerator // divisor

    @numerator.setter
    def numerator(self, numerator):
        if not isinstance(numerator, int):
            raise TypeError("illegal type numerator")
        self.__numerator = numerator
        self.__store()

    @denumerator.setter
    def denumerator(self, denumerator):
        if not isinstance(denumerator, int):
            raise TypeError("illegal type denumerator")
        if denumerator == 0:
            raise ZeroDivisionError("denumerator == 0")
        self.__denumerator = denumerator
        self.__store()

    def __str__(self):
        return str(self.__numerator) + "/" + str(self.__denumerator)

    def to_float_format(self) -> float:
        return self.__numerator / self.__denumerator

    def __eq__(self, other):
        if not isinstance(other, Rational):
            return NotImplemented
        if(self.numerator == other.numerator and self.denumerator == other.denumerator):
            return True
        else:
            return False

    def __mul__(self, other):
        if not isinstance(other,Rational):
            return NotImplemented
        return Rational(self.numerator * other.numerator, self.denumerator * other.denumerator)

    def __truediv__(self, other):
        if not isinstance(other,Rational):
            return NotImplemented
        return Rational(self.numerator * other.denumerator, self.denumerator * other.numerator)

    def __add__(self, other):
        if not isinstance(other,Rational):
            return NotImplemented
        lcd = abs(other.denumerator * self.denumerator) // math.gcd(other.denumerator, self.denumerator)
        return Rational(int(lcd/self.denumerator*self.numerator + lcd/other.denumerator*other.numerator), lcd)

    def __sub__(self, other):
        if not isinstance(other,Rational):
            return NotImplemented
        lcd = abs(other.denumerator * self.denumerator) // math.gcd(other.denumerator, self.denumerator)
        return Rational(int(lcd / self.denumerator - self.numerator + lcd/other.denumerator * other.numerator), lcd)

    def __floordiv__(self, other):
        if not isinstance(other,Rational):
            return NotImplemented
        rat = self.__truediv__(self,other)
        return Rational(rat.numerator // rat.numerator)

    def __isub__(self, other):
        if not isinstance(other, Rational):
            return NotImplemented
        lcd = abs(other.denumerator * self.denumerator) // math.gcd(other.denumerator, self.denumerator)
        self.__numerator=int(lcd / self.denumerator * self.numerator + lcd / other.denumerator * other.numerator)
        self.__denumerator = lcd
        self.__store()
        return self

    def __iadd__(self, other):
        if not isinstance(other, Rational):
            return NotImplemented
        lcd = abs(other.denumerator * self.denumerator) // math.gcd(other.denumerator, self.denumerator)
        self.__numerator = int(lcd / self.denumerator * self.numerator + lcd / other.denumerator * other.numerator)
        self.__denumerator = lcd
        self.__store()
        return self


    def __imul__(self, other):
        if not isinstance(other, Rational):
            return NotImplemented
        self.__numerator = self.numerator * other.numerator
        self.__denumerator = self.denumerator * other.denumerator
        self.__store()
        return self

    def __idiv__(self, other):
        temp  = self.__truediv__(other)
        self.__numerator = temp.numerator
        self.__denumerator = temp.denumerator
        self.__store()
        return self

    def __ifloordiv__(self, other):
        self.__numerator == self.__floordiv__(other).numerator
        self.__denumerator =  1

    def __ne__(self, other):
        return not self.__eq__(other)
