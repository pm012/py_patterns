# from __future__ import annotations # uncomment the import if python < 3.14

class Creature:
    def __init__(self, name: str, attack:int, defense:int):
        self.name = name
        self.attack = attack
        self.defense = defense

    def __str__(self)-> str:
        return f'{self.name} ({self.attack} / {self.defense})'

class CratureModifier:
    def __init__(self, creature: Creature):
        self.creature = creature
        self.next_modifier: CratureModifier | None = None # Can be None

    def add_modifier(self, modifier: CratureModifier):
        if self.next_modifier: # Singly linked list (Unidirectional list)
            self.next_modifier.add_modifier(modifier)
        else:
            self.next_modifier = modifier

    def handle(self):
        if self.next_modifier:
            self.next_modifier.handle() # if next_modifier is present call it (one key features of chain responsisbility pattern)


class NoBonussesModifier(CratureModifier):
    def handle(self):
        print('No bonuses for you') # handle from parent CreatureModifier is not called (flush chain= CoR — breaks the chain)


class DoubleAttackModifier(CratureModifier):
    def handle(self):
        print(f'Doubling {self.creature.name}''s attack')
        self.creature.attack *= 2
        super().handle() # Modifies attack and handles next handler

class IncreaseDefenseModifier(CratureModifier):    

    def handle(self):
        if self.creature.attack <=2:
            print(f'Increasing {self.creature.name} defence')
            self.creature.defense += 1
        super().handle() # Modifies defence and handles next handler

if __name__ == '__main__':
    goblin = Creature('Goblin', 1,1)
    print(goblin)

    root = CratureModifier(goblin)
    root.add_modifier(NoBonussesModifier(goblin)) #prevents bonunses modification for next modifiers

    root.add_modifier(DoubleAttackModifier(goblin))
    root.add_modifier(IncreaseDefenseModifier(goblin))
    root.add_modifier(DoubleAttackModifier(goblin))

    root.handle()
    print(goblin)
