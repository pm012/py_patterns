class CEO:
    __shared_state = {
        'name': 'Steve',
        'age': 55
    }

    def __init__(self) -> None:
        # Assign the shared state to the instance's __dict__ attribute
        # __dict__ is a special attribute that stores an object's attributes in a dictionary        
        #__slots__ = ['name', 'age'] - is used to restrict the attributes that can be added to an instance of a class. It can save memory and improve performance, but it also limits the flexibility of the class. In this case, it is commented out, so the class can have any attributes added to it.
        self.__dict__ = self.__shared_state

    def __str__(self) -> str:
        return f'{self.name} is {self.age} years old'
    
class Monostate:
    _shared_state = {}

    def __new__(cls, *args, **kwargs):
        obj = super(Monostate, cls).__new__(cls, *args, **kwargs)
        obj.__dict__ = cls._shared_state
        return obj
    
class CFO(Monostate):
    def __init__(self) -> None:
        self.name = ''
        self.money_managed = 0

    def __str__(self) -> str:
        return f'{self.name} manages ${self.money_managed}'    
if __name__ == '__main__':
    # ceo1 = CEO()
    # print(ceo1)

    # ceo2 = CEO()
    # ceo2.age = 77

    # print(ceo1)
    # print(ceo2)

    cfo1 = CFO()
    cfo1.name = 'Shery'
    cfo1.money_managed = 1
    print(cfo1)

    cfo2 = CFO()
    cfo2.name = 'Ruth'
    cfo2.money_managed = 10
    print(cfo1, cfo2, sep = '\n')