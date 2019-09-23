try :from . util import *
except ImportError: from util import *

class FactorNode():
    # __slots__ = ['data','node','factor']

    def __init__(self,number):
        self.data = int(number)
        self.node = None
        self.factor = []
        self.lookIn()

    # @timer
    def lookIn(self):
        # if not isPrime(int(abs(self.data))):
        afterMul = -1 if abs(self.data) != self.data else 1

        primes = filter(isPrime, [prime for prime in range(int(abs(self.data)))])
        # primes = [prime for prime in range(int(abs(self.data)))]

        for i in primes:
            if i != 0 and i != 1:
                if self.data/i == self.data//i and i > 1:
                    self.node = self.__class__(abs(self.data)/i)
                    self.factor.append(i*afterMul)
                    self.factor = [ i*afterMul ]
                    break

        # else:
        #     self.data = 1

    # @timer
    def lowerNode(self):
        if self.node != None:
            output = self.factor
            output.extend(self.node.lowerNode())

            return output

        else:
            return [self.data]

    def __str__(self):
        if self.node != None:
            return f'me : ({self.data}) factor : ({self.factor})\nnode : (\n{str(self.node)}\n)'
        else:
            return f'me : ({self.data}) factor : ({self.factor}) node : (NULL)'


if __name__ == "__main__":
    from random import randint


    for i in range(1):
        i += 2

        runtime = randint(0,10**i)


        instance = FactorNode(runtime)
        print(instance.lowerNode(), listMulti(instance.lowerNode()), ' - - - - - - - - ',runtime)
        
        del instance










