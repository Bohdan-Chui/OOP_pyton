from Rational import  Rational

if __name__ == '__main__':

    print(Rational(2,4) != Rational(1,2))
    rational = Rational(2,6)
    print(rational)
    rational+=Rational(1,6)
    print(rational)
    print((Rational(1,4)/ Rational(1,4)).to_float_format())
    print(Rational(1,6) + Rational(2,6))
