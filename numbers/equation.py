from .  util import *
from .Number import Number


class UnassignmentError(Exception): pass

class Opperation:
    def __init__(self, oppFCF):
        self.function = oppFCF
        self.isopperation = True
    
    def __call__(self,*args,**kwargs):
        return self.function(*args,**kwargs)


class OpperationFactory:
    @classmethod
    @Opperation
    def add(n1,n2):
        return n1 + n2

    @classmethod
    @Opperation
    def subtract(n1,n2):
        return n1 - n2


    @classmethod
    @Opperation
    def multiply(n1,n2):
        return n1 * n2

    @classmethod
    @Opperation
    def divide(n1,n2):
        return n1 / n2

    @classmethod
    @Opperation
    def power(n1,n2):
        return n1 ** n2

    @classmethod
    @Opperation
    def root(n1,n2):
        return n1**(1/n2)

class Equation:
    @classmethod
    def fromSpecal(cls,number1 ,number2,opperation):
        def buildNumber(num):
            return Number.fromInt(num)

        if isinstance(number1,int):
            factors1 = buildNumber(number1)
        
        else: factors1 = number1

        if isinstance(number2,int):
            factors2 = buildNumber(number2)
        
        else: factors2 = number2

        return cls(factors1, factors2,opperation)

    def __init__(self, n1, n2 = None, opperation = None):
        self.number1 = n1
        self.number2 = n2
        if callable(opperation):
            self.opperation = opperation
            
        else: raise ValueError

    @property
    def factors(self):
        return [self.number1.factors,self.number2.factors,self.opperation]

    @property
    def value(self):
        try:
            return self.opperation(self.number1,self.number2)

        except TypeError:
            return self.opperation(self.number1)



if __name__ == "__main__":
    print(Equation.fromSpecal(23,23,OpperationFactory.divide).factors)