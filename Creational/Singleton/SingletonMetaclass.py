class Singleton(type):
    _instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super(Singleton, cls).__call__(*args, **kwargs)
        return cls._instances[cls]
    
# metaclass defines how the class should behave 
# In the example below Database class will inherit behavior of __call__ method of Singleton class
class Database(metaclass=Singleton):
    def __init__(self):
        print('Loading database')

if __name__ == '__main__':
    d1 = Database()
    d2 = Database()
    print(d1 == d2)