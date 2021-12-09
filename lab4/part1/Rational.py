from math import gcd


class Rational:

    def __init__(self, numerator=0, denominator=1):
        self.numerator = numerator
        self.denominator = denominator
        self.__gcd()

    @property
    def numerator(self):
        return self.__numerator

    @numerator.setter
    def numerator(self, value):
        if not isinstance(value, int):
            raise TypeError('numerator must be of type int')
        self.__numerator = value

    @property
    def denominator(self):
        return self.__denominator

    @denominator.setter
    def denominator(self, value):
        if not isinstance(value, int):
            raise TypeError('denominator must be of type int')
        if not value:
            raise ZeroDivisionError("denominator cannot be 0")
        self.__denominator = value

    def __gcd(self):
        if self.numerator:
            divisor = gcd(self.numerator, self.denominator)
            self.numerator = self.numerator // divisor
            self.denominator = self.denominator // divisor

    def __str__(self):
        return f'{self.__numerator} / {self.__denominator}'

    def get_float(self):
        return self.__numerator / self.__denominator

    def __eq__(self, other):
        if isinstance(other, Rational):
            return self.numerator / self.denominator == other.numerator / other.denominator
        if isinstance(other, int):
            return self.numerator / self.denominator == other
        raise TypeError('other must be of type Rational or int')

    def __ne__(self, other):
        return not self.__eq__(other)

    def __mul__(self, other):
        if isinstance(other, Rational):
            return Rational(self.numerator * other.numerator, self.denominator * other.denominator)
        if isinstance(other, int):
            return Rational(self.numerator * other, self.denominator)
        raise TypeError('other must be of type Rational or int')

    def __truediv__(self, other):
        if isinstance(other, Rational):
            return Rational(self.numerator * other.denominator, self.denominator * other.numerator)
        if isinstance(other, int):
            return Rational(self.numerator, self.denominator * other)
        raise TypeError('other must be of type Rational or int')

    def __add__(self, other):
        if isinstance(other, Rational):
            return Rational(self.numerator * other.denominator + self.denominator * other.numerator,
                            self.denominator * other.denominator)
        if isinstance(other, int):
            return Rational(self.numerator + self.denominator * other, self.denominator)
        raise TypeError('other must be of type Rational or int')

    def __sub__(self, other):
        if isinstance(other, Rational):
            return Rational(self.numerator * other.denominator - self.denominator * other.numerator,
                            self.denominator * other.denominator)
        if isinstance(other, int):
            return Rational(self.numerator - self.denominator * other, self.denominator)
        raise TypeError('other must be of type Rational or int')

    def __isub__(self, other):
        if isinstance(other, Rational):
            self.numerator = self.numerator * other.denominator - self.denominator * other.numerator
            self.denominator = self.denominator * other.denominator
            self.__gcd()
            return self
        if isinstance(other, int):
            self.numerator = self.numerator - self.denominator * other
            self.denominator = self.denominator
            self.__gcd()
            return self
        raise TypeError('other must be of type Rational or int')

    def __iadd__(self, other):
        if isinstance(other, Rational):
            self.numerator = self.numerator * other.denominator + self.denominator * other.numerator
            self.denominator = self.denominator * other.denominator
            self.__gcd()
            return self
        if isinstance(other, int):
            self.numerator = self.numerator + self.denominator * other
            self.denominator = self.denominator
            self.__gcd()
            return self
        raise TypeError('other must be of type Rational or int')

    def __imul__(self, other):
        if isinstance(other, Rational):
            self.numerator = self.numerator * other.numerator
            self.denominator = self.denominator * other.denominator
            self.__gcd()
            return self
        if isinstance(other, int):
            self.numerator = self.numerator * other.numerator
            self.denominator = self.denominator
            self.__gcd()
            return self
        raise TypeError('other must be of type Rational or int')

    def __idiv__(self, other):
        if isinstance(other, Rational):
            self.numerator = self.numerator * other.denominator
            self.denominator = self.denominator * other.numerator
            self.__gcd()
            return self
        if isinstance(other, int):
            self.denominator = self.denominator * other.numerator
            self.__gcd()
            return self
        raise TypeError('other must be of type Rational or int')
