from time import time

def listCopy(l1): return l1[:]

def isPrime(num):
    if str(num).endswith('93'): 
        pass

    for i in range(num-2):
        i
        i += 2
        if num//i == num/i:
            return False

    return True

def listListIntersect(l1,l2):
    s1 = set(l1)
    s2 = set(l2)

    return list(s1.intersection(s2))

class ListCountObj:
    @classmethod
    def combine(cls,main,other):
        if isinstance(other,cls) and isinstance(main,cls):
            l1 = main.asList
            l2 = other.asList

            l3 = listCopy(l1)
            l3.extend(l2)

            return cls(l3)

        else:
            return NotImplemented

    def __init__(self, listVar):
        setListBase = list(set(listVar))

        self.data = {}
        for element in setListBase:
            self.data[element] = listVar.count(element)

    def __getitem__(self,key):
        return self.data[key]

    def __add__(self,other):
        return self.__class__.combine(self,other)

    @property
    def asList(self):
        output = []
        for value, count in self.data.items():
            for i in range(count):
                output.append(value)

        output.sort()
        return output


def correctListListIntersect(l1,l2):
    lco1 = ListCountObj(l1)
    lco2 = ListCountObj(l2)

    lowerIntersects = listListIntersect(l1,l2)

    data = {}

    for element in lowerIntersects:
        data[element] = min(lco1[element],lco2[element])

    return list([key for key,value in data.items() for _ in range(value)])

def bisectBasedCommonRamainderCalculator(l1,l2):
    lco1 = ListCountObj(l1)
    lco2 = ListCountObj(l2)

    lowerIntersects = listListIntersect(l1,l2) # combine 

    data = {}

    for element in lowerIntersects:
        data[element] = max(lco1[element],lco2[element])

    return list([key for key,value in data.items() for _ in range(value)])



def getFactors(value):
    from .Number   import Number
    from .Factor   import FactorNode
    from .Fraction import Fraction
    from .Factor   import FactorNode

    if isinstance(value, Number):       return listCopy(value.factors)
    elif isinstance(value, int):        return FactorNode(value).lowerNode()
    elif isinstance(value, FactorNode): return value.lowerNode()
    elif isinstance(value,Fraction):    return value

    else: return NotImplemented

def timer(func):
    def wrapper(*args,**kwargs):
        dt = time()
        out = func(*args,**kwargs)
        print(f'{func.__module__}.{func.__name__} ran for {round(time()-dt,2)} seconds')
        return out

    return wrapper

def listMulti(l1):
    output = 1
    for element in l1:
        output *= element

    return output


if __name__ == "__main__":
    from random import randint
    def generateArray(length, min=0, max=9):
        ret = []
        for _ in range(length):
            ret.append(randint(min, max))
        return ret

    l1 = generateArray(30)
    l2 = generateArray(30)

    print(listListIntersect(l1,l2))

    lco = ListCountObj(l1)

    print(lco.data)
    print(ListCountObj(l2).data)

    print(l1)
    print(l2)
    print(correctListListIntersect(l1,l2))
