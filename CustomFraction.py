# import math


def find_decimal(f: float):
    if f == int(f):
        f = int(f)
        return 0
    else:
        f = str(float(f))
        return len(f) - 1 - f.find('.')


def gcd(m, n):
    while m % n != 0:
        oldm = m
        oldn = n

        m = oldn
        n = oldm % oldn
    return n


class Fraction:
    def __init__(self, top, bottom):
        if isinstance(top, int) and isinstance(bottom, int):
            sign = -1 if top * bottom < 0 else 1
            top = abs(top)
            bottom = abs(bottom)
            common = gcd(top, bottom)
            self.num = sign * top // common
            self.den = bottom // common
        else:
            raise ValueError('Bad numerator or denominator ')

    def __str__(self):
        return str(self.num) + "/" + str(self.den)

    def show(self):
        print(self.num, "/", self.den)

    def __add__(self, otherfraction):
        if not isinstance(otherfraction, Fraction):
            return otherfraction + self
        newnum = self.num * otherfraction.den + \
                 self.den * otherfraction.num
        newden = self.den * otherfraction.den
        common = gcd(newnum, newden)
        return Fraction(newnum // common, newden // common)

    def __eq__(self, other):
        firstnum = self.num * other.den
        secondnum = other.num * self.den

        return firstnum == secondnum

    def getNum(self):
        return self.num

    def getDen(self):
        return self.den

    def __sub__(self, other):
        newnum = self.num * other.den - \
                 self.den * other.num
        newden = self.den * other.den
        common = gcd(newnum, newden)
        return Fraction(newnum // common, newden // common)

    def __mul__(self, other):
        newnum = self.num * other.num
        newden = self.den * other.den
        common = gcd(newnum, newden)
        return Fraction(newnum // common, newden // common)

    def __truediv__(self, other):
        newnum = self.num * other.den
        newden = self.den * other.num
        common = gcd(newden, newnum)
        return Fraction(newnum // common, newden // common)

    def __gt__(self, other):
        return (self - other).num > 0

    def __ge__(self, other):
        return (self - other).num >= 0

    def __lt__(self, other):
        return (self - other).num < 0

    def __le__(self, other):
        return (self - other).num <= 0

    def __ne__(self, other):
        return (self - other).num != 0

    def __radd__(self, other: float):
        d_num = find_decimal(other)
        other = Fraction(int(round(other * 10 ** d_num, 0)), 10 ** d_num)
        return other + self

    def __iadd__(self, other):
        return self + other

    def __repr__(self):
        return 'Fracton {}/{}'.format(self.num, self.den)


if __name__ == '__main__':
    f = Fraction(2, 3)
    f += Fraction(1, 3)
    print(repr(f))
