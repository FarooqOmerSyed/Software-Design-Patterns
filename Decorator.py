"""
Decorator Design Pattern
"""

# create an Undecorated Object
class UndecoratedObject:
    @staticmethod
    def get():
        return "Undecorated Object"


# Decorated Wrapper
class DecoratedObject:
    def __init__(self, undecorated):
        self.undecorated = undecorated

    def get(self):
        return self.undecorated.get().replace("Undecorated", "Decorated")


# create the instance of UndecoratedObject

Undecorated = UndecoratedObject()
print(Undecorated.get())


# create the instance of Decorated wrapper
Decorated = DecoratedObject(Undecorated)
print(Decorated.get())