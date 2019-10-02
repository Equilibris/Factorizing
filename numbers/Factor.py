try :from . util import *
except ImportError: from util import *
from time import sleep

class FactorNode():
    # __slots__ = ['data','node','factor']

    def __init__(self,number):
        self.data = int(number)
        self.node = None
        self.factor = []
        self.lookIn()

##    @timer
    def lookIn(self):
        # @Memoize
        def getFactors(data):
            afterMul = -1 if abs(self.data) != self.data else 1

            if str(self.data).endswith('0'):
                tempData = int(self.data/10)
                self.factor.extend([2*afterMul,5])

                loopCount = 1

                while str(tempData).endswith('0'):
                    self.factor.extend([2*afterMul,5])
                    tempData = int(tempData//10)
                    loopCount += 1

                self.node = self.__class__(abs(self.data)/10**loopCount)

            elif str(self.data).endswith('2'):
                tempData = int(self.data//2)
                self.factor.extend([2*afterMul])

                loopCount = 1

                while str(tempData).endswith('2'):
                    self.factor.extend([2])
                    tempData = int(tempData//2)
                    loopCount += 1

                self.node = self.__class__(abs(self.data)/2**loopCount)

            # elif str(self.data).endswith('93'): pass

            elif not isPrime(self.data):
                # primes = filter(isPrime, [prime for prime in range(int(abs(self.data)))])
                # primes = [prime for prime in range(int(abs(self.data))) if isPrime(prime)]
                # primes = [p for p in range(int(abs(self.data)))]

                for i in range(int(abs(self.data))):
                    if i != 0 and i != 1:
                        if self.data/i == self.data//i and i > 1 and int(self.data/i) != 1:
                        # if self.data % i == 0 and i > 1:
                            # print(abs(self.data)/i, i)
                            self.node = self.__class__(abs(self.data)/i)
                            self.factor.append(i*afterMul)
                            break

            else:
                # self.node = None
                # self.factor.append()
                pass

        getFactors(self.data)

    # @timer
    def oldLowerNode(self): 
        if self.node != None:
            output = listCopy(self.factor)
            print('pre\t',output)

            node = listCopy(self.node.oldLowerNode())

            print('adding\t', node)
            output.extend(node)
            print('post\t', output)


            # assert listMulti(output) > self.data, 'error found'

            return output

        else: return [self.data]

    def lowerNode(self): # new lower node
        if self.node != None:
            nodeData = self.node.lowerNode()

            nodeData.extend(self.factor)

            return nodeData
        else:
            return [ self.data ]

    def __str__(self):
        if self.node != None:
            return f'me : ({self.data}) factor : ({self.factor})\nnode : (\n{str(self.node)}\n)'
        else:
            return f'me : ({self.data}) factor : ({self.factor}) node : (NULL)'


if __name__ == "__main__":
    from random import randint

    # tempList = FactorNode(1508000000000).lowerNode()
    # print(tempList,listMulti(tempList))

    for i in range(14,30):
        runtimeVar = randint(10**(i-1),10**i)

##        print(runtimeVar)
        instance = FactorNode(runtimeVar)

        instanceData = instance.lowerNode()

        print('truth : ',i, instanceData)

##        sleep(2)










        
