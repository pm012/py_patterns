def singleton(class_):
    instaces = {}

    def get_instance(*args, **kwargs):
        if class_  not in instaces:
            instaces[class_] = class_(*args, **kwargs)
        return instaces[class_]
    
    return get_instance

@singleton
class Database:
    def __init__(self) -> None:
        print('Loading database')

@singleton
class Pool:
    def __init__(self, id:int)-> None:
        print('Setting id for pool')
        self.id = id


if __name__ == '__main__':
    d1 = Database()
    d2 = Database()
    print(d1 == d2)

    p1 = Pool(1)
    p2 = Pool(2)
    print(p1 == p2)