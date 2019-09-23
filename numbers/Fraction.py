from .     util import *
from .numberABC import NumbersBase
from .   Factor import FactorNode
from .   Number import Number
from . equation import Equation, OpperationFactory
from copy       import copy
# from copy import copy


class Fraction:
    @classmethod
    def fromSpecal(cls,numerator ,denominator):
        return cls(getFactors(numerator),getFactors(denominator))

    # __slots__ = ['factors']

    def __init__(self, numeratorFactors, denominatorFactors):
        self.factors = [numeratorFactors,denominatorFactors]
        
        self = self.simplyfy()

    @property
    def value(self):
        numerator = 1
        if not isinstance(self.factors[0],Fraction):
            for num in self.factors[0]:
                numerator *= num
        
        else:
            numerator = self.factors[0].value

        denominator = 1
        if not isinstance(self.factors[1],Fraction):
            for num in self.factors[1]:
                denominator *= num

        else:
            denominator = self.factors[1].value

        return numerator/denominator if denominator != 1 else numerator if denominator != 0 else ZeroDivisionError

    def simplyfy(self):
        if not isinstance(self.factors[0],Fraction) and not isinstance(self.factors[1],Fraction):
            commons = correctListListIntersect(self.factors[0],self.factors[1])

            for element in commons:
                self.factors[0].remove(element)
                self.factors[1].remove(element)

            if self.factors[1] == [] or self.factors[1] == [1]:
                return Number(self.factors[0])
            
            else: return self

            # return self

        return NotImplemented

    def __add__(self, other):
        if isinstance(other,Number) or isinstance(other,int):
            return Equation.fromSpecal(self,other,OpperationFactory.add)

        else:
            return NotImplemented

    def __sub__(self,other):
        if isinstance(other,Number) or isinstance(other,int):
            return Equation.fromSpecal(self,other,OpperationFactory.subtract)

        else:
            return NotImplemented

    def __mul__(self,other):
        if isinstance(other,Number) or isinstance(other,int) or isinstance(other,FactorNode):
            factors = getFactors(other)

            if not isinstance(self.factors[1],Fraction):
                denominator = listCopy(self.factors[1])

            else:
                denominator = copy(self.factors[1])

            if not isinstance(self.factors[0],Fraction):
                numerator = listCopy(self.factors[0])
                numerator.extend(factors)

            else:
                numerator = copy(self.factors[0])
                numerator *= numerator(factors)
            
            # denominator.extend(factors)

            return self.__class__(numerator,denominator)

        elif isinstance(other,Fraction):
            otherNumerator = listCopy(other.factors[0])
            otherDenominator = listCopy(other.factors[1])

            if not isinstance(self.factors[0],Fraction):
                numerator = listCopy(self.factors[0])
                numerator.extend(otherNumerator)

            else:
                numerator = copy(self.factors[0])
                numerator *= Number(otherNumerator)


            if not isinstance(self.factors[1],Fraction):
                denominator = listCopy(self.factors[1])
                denominator.extend(otherDenominator)

            else:
                denominator = copy(self.factors[1])
                denominator *= Number(otherDenominator)

            return self.__class__(numerator,denominator)

        else:
            return NotImplemented

    def __truediv__(self, other):
        if not isinstance(other,Fraction):
            me = self
            notMe = other

            fracton = Fraction.fromSpecal(self,other)

            self = me
            other = notMe
            return fracton

        else:
            otherNumerator = listCopy(other.factors[0])
            otherDenominator = listCopy(other.factors[1])
            invertedOther = Fraction(otherDenominator, otherNumerator)

            return self*invertedOther

