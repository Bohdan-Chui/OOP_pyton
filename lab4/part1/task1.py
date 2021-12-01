from Rational import  Rational

if __name__ == '__main__':
    try:
        print(Rational(2,4) != Rational(1,2))
        rational = Rational(1,6)
        rational += Rational(1,6)
        print(rational)
        print((Rational(1,4)/ Rational(1,4)).to_float_format())
        print(Rational(2,5) + Rational(2,6))
    except Exception as ve:
        print(ve)