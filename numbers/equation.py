class UnassignmentError(Exception): pass

class Opperation:
    def __init__(self, oppFCF):
        self.function = oppFCF
        self.isopp = True
    
    def __call__(self,*args,**kwargs):
        return self.function(*args,**kwargs)


class OpperationFactory:
    @classmethod
    @Opperation
    def add(n1,n2):
        pass

    @classmethod
    @Opperation
    def subtract(n1,n2):
        pass


    @classmethod
    @Opperation
    def multiply(n1,n2):
        pass

    @classmethod
    @Opperation
    def divide(n1,n2):
        pass

    @classmethod
    @Opperation
    def power(n1,n2):
        pass

    @classmethod
    @Opperation
    def power(n1,n2):
        pass

    @classmethod
    @Opperation
    def root(n1,n2):
        pass

class Equation:
    @classmethod
    def fromSpecal(cls,number1 ,number2,opperation):
        return cls(getFactors(number1), getFactors(number2),opperation)

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
    print(Equation(23,23,OpperationFactory.divide).factors)