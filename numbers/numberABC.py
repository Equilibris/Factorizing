class subclasserror(Exception): pass

def abcTest(instance,_cls):
    if instance.__class__ == _cls:
        raise subclasserror

class NumbersBase: 
    def __init__(self):
        abcTest(self,NumbersBase)

if __name__ == "__main__":
    pass

