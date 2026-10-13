from abc import ABC
from enum import Enum, auto


class HotDrink(ABC):
    def consume(self):
        pass


class Tea(HotDrink):
    def consume(self):
        print('This tea is delicious')


class Coffee(HotDrink):
    def consume(self):
        print('This coffee is delicious')

# In Python it is not necessary. We can remove it safely (and remove from the inherited classes). But it must be used in strictly typed languages
class HotDrinkFactory(ABC):
    def prepare(self, amount):
        pass


class TeaFactory(HotDrinkFactory):
    def prepare(self, amount):
        print(f' Put in tea bag, boil water,'
              f' pour {amount}(ml), enjoy!')
        return Tea()


class CoffeeFactory(HotDrinkFactory):
    def prepare(self, amount):
        print(f' Grind some beans,  boil water,'
              f' pour {amount}(ml), enjoy!')
        return Coffee()

class LatteFactory(HotDrinkFactory):
    def prepare(self, amount):
        milk_amount = (amount//180)*20
        print(f'Grind some beans, boil water, pour {amount}(ml), add some {milk_amount}(ml) of milk and enjoy!')


def make_drink(type):
    if type == 'tea':
        return TeaFactory().prepare(200)
    elif type == 'coffee':
        return CoffeeFactory().prepare(50)
    else:
        return None

class HotDrinkMachine:
    class AvailableDrink(Enum):
        COFFEE = auto()
        TEA = auto()
        LATTE = auto()
    factories = []
    initialized = False

    def __init__(self):
        if not self.initialized:
            self.initialized = True
            for d in self.AvailableDrink:
                name = d.name[0] + d.name[1:].lower()
                factory_name = name + 'Factory'
                factory_instance = eval(factory_name)()
                self.factories.append((name, factory_instance))

    def make_drink(self):
        print('Available drinks:')
        idx = 0
        for f in self.factories:
            idx += 1
            print(f'{idx}: {f[0]}')
            
        s = input(f'Please, pick a drink ( 1 - {len(self.factories)}): ')
        idx = int(s)
        s = input(f'Specify amount: ')
        amount = int(s)
        return  self.factories[idx-1][1].prepare(amount)


if __name__ == '__main__':
    # entry = input('What kind of drink would you like?')
    # drink = make_drink(entry)

    hdm = HotDrinkMachine()
    hdm.make_drink()

