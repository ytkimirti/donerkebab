class BaseClass:
    myvar = "hello"

    def add(self, a, b):
        print(f"{a} + {b} = {a + b}")
        return a + b

class Child(BaseClass):
    def __init__(self):
        super()

    def add(self, a, b):
        super().add(a, myvar)

c = Child()

c.add(2, 3)