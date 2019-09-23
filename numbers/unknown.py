class Unknown:
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return self.name

class Variable(Unknown):
    def __init__(self, name, value):
        super().__init__(name)
        self.value = value

    def __repr__(self):
        return f'{self.name} = {self.value}'