import random
class Database:
    _instance = None

    def __init__(self) -> None:
        id = random.randint(1, 101)
        print('Loading a database from file')
        print(f'id={id}')

    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            cls._instance = super(Database, cls).__new__(cls, *args, **kwargs)
        return cls._instance
    
if __name__=='__main__':
    d1 = Database()
    d2 = Database()
    print(d1 == d2)

#we can see here that the initializer is called anyway
