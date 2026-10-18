# event broker (observer)
# cqs - command query separation
# from __future__ import annotations # uncomment the import if python < 3.14
from enum import Enum
from abc import ABC

class Event(list): # Event is a list of callable subscribers/handlers
    def __call__(self, *args, **kwargs):
        for item in self: # Item should be callable
            item(*args, **kwargs)


class WhatToQuery(Enum):
    ATTACK = 1
    DEFENSE = 2


class Query:
    def __init__(self, creature_name:str, what_to_query: WhatToQuery, default_value:int): 
        self.value = default_value #default_value = initial state, self.value = current state (mutable)
        self.what_to_query = what_to_query
        self.creature_name = creature_name

        

class Game:
    def __init__(self):
        self.queries = Event()

    def perform_query(self, sender, query:Query): # sender is currently Creature, but it would be better to create GameObject as abstract with descendants like (Creature, Building, Spell...)
        self.queries(sender, query)

class CreatureModifier(ABC):
    def __init__(self, game:Game, creature:Creature):
        self.game = game
        self.creature = creature
        self.game.queries.append(self.handle)

    def handle(self, sender, query:Query):
        pass

    def __enter__(self)->CreatureModifier:
        return self

    def __exit__(self, exc_type, exc, tb):
        self.game.queries.remove(self.handle)

class DoubleAttackModifier(CreatureModifier):
    def handle(self, sender, query: Query):
        if sender.name == self.creature.name and \
            query.what_to_query == WhatToQuery.ATTACK:
            query.value *= 2


class Creature:
    def __init__(self, game: Game, name: str, attack:int, defense:int):
        self.game = game
        self.name = name
        self.initial_attack = attack
        self.initial_defense = defense

    @property # CQS Query: creates a temporary state query, broadcasts it via Broker, and returns final value
    def attack(self)->int:
        # query
        q = Query(self.name, WhatToQuery.ATTACK, self.initial_attack)
        self.game.perform_query(self, q)

        return q.value


    @property
    def defense(self)->int:
        # query
        q = Query(self.name, WhatToQuery.DEFENSE, self.initial_defense)
        self.game.perform_query(self, q) 
    
        return q.value

    def __str__(self)->str:
        return f'{self.name} ({self.attack}/{self.defense})'


if __name__ == "__main__":
    game = Game()
    goblin = Creature(game, 'Strong Goblin', 2, 2)
    print(goblin)

    with DoubleAttackModifier(game, goblin):
        print(goblin)
    print(goblin)


        
