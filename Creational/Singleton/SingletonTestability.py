from typing import Any
import unittest

FILE_PATH = './Creational/Singleton/TestabilityDB/capitals.txt'
class Singleton(type):
    _instances = {}

    def __call__(cls, *args: Any, **kwds: Any) -> Any:
        if cls not in cls._instances:
            cls._instances[cls] = super(Singleton, cls).__call__(*args, **kwds)
        return cls._instances[cls]
    
class Database(metaclass = Singleton):
    def __init__(self):
        #self.file_path = 
        self.population = {}
        f = open (FILE_PATH, 'r')
        lines = f.readlines()
        for i in range(0, len(lines), 2):
            self.population[lines[i].strip()] = int(lines[i+1].strip())
        f.close()

class SingletonRecordFinder:
    def total_population(self, cities):
        result = 0
        for c in cities:
            result += Database().population[c]
        return result
    
class ConfigurableRecordFinder:
    def __init__(self, db = Database()) -> None:
        self.db = db

    def total_population(self, cities):
        result = 0
        for c in cities:
            result += self.db.population[c]
        return result
    
class DummyDatabase:
    population = {
        'alpha': 1,
        'beta': 2,
        'gamma': 3
    }

    def get_population(self, name):
        return self.population[name]

class SingletonTests(unittest.TestCase):
    def test_is_singleton(self):
        db1 = Database()
        db2 = Database()
        self.assertEqual(db1, db2)

    # This approach may not work because data in the live database can be changed and tests will fail
    def test_singleton_total_population(self):
        rf = SingletonRecordFinder()
        names = ['Seoul', 'Mexico City']
        tp = rf.total_population(names)
        self.assertEqual(17500000+17400000, tp)
    
    ddb = DummyDatabase()
    
    def test_dependent_tatal_population(self):
        crf = ConfigurableRecordFinder(self.ddb)
        self.assertEqual(3, crf.total_population(['alpha', 'beta']))




if __name__ == '__main__':
   unittest.main()
