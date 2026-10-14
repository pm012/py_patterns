"""
Consider the code presented below. We have two classes called SingleValue and ManyValues. SingleValue stores just one numeric value, but ManyValues can store
 either numeric values or SingleValue objects.

You are asked to give both SingleValue and ManyValues a property member called sum that returns a sum of all the values that the object contains. 
Please ensure that there is only a single method that realizes the property sum, not multiple methods.

Here is a sample unit test:

class FirstTestSuite(unittest.TestCase):
    def test(self):
        single_value = SingleValue(11)
        other_values = ManyValues()
        other_values.append(22)
        other_values.append(33)
        # make a list of all values
        all_values = ManyValues()
        all_values.append(single_value)
        all_values.append(other_values)
        self.assertEqual(all_values.sum, 66)
"""
from abc import ABC
import unittest
class Countable(ABC):
    @property
    def sum(self):
        res = 0
        for items in self:
            if isinstance(items, Countable):
                res += items.sum
            else:            
                res += items
        return res


class SingleValue(Countable):
    def __init__(self, value):
        self.value = value

    def __iter__(self):
        yield self.value

class ManyValues(list, Countable):
    def __init__(self):
        super().__init__()

class FirstTestSuite(unittest.TestCase):
    def test(self):
        single_value = SingleValue(11)
        
        other_values = ManyValues()
        other_values.append(22)
        other_values.append(33)
        
        # Перевіримо проміжну суму (числа + ManyValues)
        self.assertEqual(other_values.sum, 55)
        
        # Збираємо все разом
        all_values = ManyValues()
        all_values.append(single_value)
        all_values.append(other_values)
        
        # Фінальна перевірка, як у завданні (.sum без дужок)
        self.assertEqual(all_values.sum, 66)
        

if __name__ == "__main__":
    single_value = SingleValue(11)
    other_values = ManyValues()
    other_values.append(22)
    other_values.append(33)
    # make a list of all values
    all_values = ManyValues()
    all_values.append(single_value)
    all_values.append(other_values)
    all_values.append(99)
    print(all_values.sum)
    
    suite = unittest.TestLoader().loadTestsFromTestCase(FirstTestSuite)
    unittest.TextTestRunner().run(suite)
    