from .   Factor import FactorNode
from .numberABC import NumbersBase

class Number(NumbersBase):
    @classmethod
    def fromInt(cls, _int):
        return cls(FactorNode(_int).lowerNode())
    
    @classmethod
    def fromFloat(cls,_float):
        from .Fraction import Fraction

        ratio = float(_float).as_integer_ratio()
        return Fraction.fromSpecal(ratio[0],ratio[1])

    # __slots__ = ['factors']

    def __init__(self, factors):
        self.factors = factors

    @property
    def value(self):
        output = 1
        for num in self.factors:
            output *= num

        return output

    def __add__(self, other):
        if isinstance(other,Number):
            return self.__class__.fromInt(self.value + other.value)

        elif isinstance(other,int):
            return self.__class__.fromInt(self.value + other)

        else:
            return NotImplemented

    def __sub__(self,other):
        if isinstance(other,Number):
            return self.__class__.fromInt(self.value - other.value)

        elif isinstance(other,int):
            return self.__class__.fromInt(self.value - other)

        else:
            return NotImplemented

    def __mul__(self,other):
        from .Fraction import Fraction

        if isinstance(other,Number):
            arr = self.factors
            arr.extend(other.factors)
            return self.__class__(arr)

        elif isinstance(other,int):
            arr = self.factors
            arr.extend(FactorNode(other).lowerNode())

            return self.__class__(arr)

        elif isinstance(other, Fraction):
            me = Fraction(self.factors,[1])
            
            return me*other
        else:
            return NotImplemented

    def __truediv__(self, other):
        from .Fraction import Fraction
        me = self
        notMe = other

        fracton = Fraction.fromSpecal(self,other)

        self = me
        other = notMe
        return fracton














