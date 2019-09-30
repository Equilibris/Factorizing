from .     util import *
from .numberABC import NumbersBase
from .   Factor import FactorNode
from .   Number import Number
from . equation import Equation, OpperationFactory
from       copy import copy
# from copy import copy


class Fraction:
    @classmethod
    def fromSpecal(cls,numerator ,denominator):
        return cls(getFactors(numerator),getFactors(denominator))

    # __slots__ = ['factors']

    def __init__(self, numeratorFactors, denominatorFactors):
        self.factors = [numeratorFactors,denominatorFactors]
        
        self.simplyfy()

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

    @property
    def fractData(self):
        valueData   = self.factors

        numerator   = listMulti(valueData[0]) if not isinstance(valueData[0],Fraction) else valueData[0].value
        denominator = listMulti(valueData[1]) if not isinstance(valueData[1],Fraction) else valueData[1].value
        
        return [numerator,denominator] 

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
        def getFromDual2DList(meFactors,otherFactors):
            multiplumDistance = CommonRamainderCalculations.calculateCommon(meFactors[1],otherFactors[1])

            # print('me',meFactors,'other',otherFactors, 'distance',multiplumDistance,sep='\n')

            meFactors[0].extend(multiplumDistance[0])
            meFactors[1].extend(multiplumDistance[0])

            otherFactors[0].extend(multiplumDistance[1])
            otherFactors[1].extend(multiplumDistance[1])

            numerator = Number.fromInt(listMulti(meFactors[0])+listMulti(otherFactors[0])).factors

            return self.__class__(numerator,meFactors[1]) # calculate multiplum and add

        if isinstance(other,Number):
            meFactors    = [listCopy(self.factors[0]), listCopy(self.factors[1])]
            otherFactors = [listCopy(other.factors),   [1]]

            return getFromDual2DList(meFactors,otherFactors)

        elif isinstance(other,int):
            meFactors    = [listCopy(self.factors[0]),     listCopy(self.factors[1])]
            otherFactors = [Number.fromInt(other).factors, [1]]

            # print('me',meFactors,'other',otherFactors,sep='\n')

            return getFromDual2DList(meFactors,otherFactors)

        elif isinstance(other,Fraction):
            meFactors    = [listCopy(self.factors[0]),  listCopy(self.factors[1])]
            otherFactors = [listCopy(other.factors[0]), listCopy(other.factors[1])]

            return getFromDual2DList(meFactors,otherFactors)

        else:
            return NotImplemented

    def __sub__(self,other):
        other = other*-1
        return self + other

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

