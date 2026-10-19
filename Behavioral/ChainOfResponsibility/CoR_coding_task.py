"""
You are given a game scenario with classes Goblin and GoblinKing. Please implement the following rules:

A goblin has base 1 attack/1 defense (1/1), a goblin king is 3/3.

When the Goblin King is in play, every other goblin gets +1 Attack.

Goblins get +1 to Defense for every other Goblin in play (a GoblinKing is a Goblin!).

Example:

Suppose you have 3 ordinary goblins in play. Each one is a 1/3 (1/1 + 0/2 defense bonus).

A goblin king comes into play. Now every goblin is a 2/4 (1/1 + 0/3 defense bonus from each other + 1/0 from goblin king)

The state of all the goblins has to be consistent as goblins are added and removed from the game.

Here is an example of the kind of test that will be run on the system:

class FirstTestSuite(unittest.TestCase):
    def test(self):
        game = Game()
        goblin = Goblin(game)
        game.creatures.append(goblin)
 
        self.assertEqual(1, goblin.attack)
        self.assertEqual(1, goblin.defense)
Note: creature removal (unsubscription) does not need to be implemented.
"""
from __future__ import annotations
from abc import ABC
import unittest
from enum import Enum

class WhatToQuery(Enum):
    ATTACK = 1
    DEFENSE = 2

class Query:
    def __init__(self, creature: Creature, what_to_query: WhatToQuery, default_value:int):        
        self.creature = creature
        self.what_to_query = what_to_query
        self.value = default_value

class Event(list):
    def __call__(self, *args, **kwargs):
        for item in self:
            item(*args, **kwargs)

class Game:
    def __init__(self):
        self.creatures = []
        self.queries = Event() # broker chain

class Creature(ABC):
    def __init__(self, game: Game, attack: int, defense: int):
        self.game = game
        self.initial_attack = attack
        self.initial_defense = defense

    @property
    def attack(self):
        query = Query(self, WhatToQuery.ATTACK, self.initial_attack)
        self.game.queries(self, query) # query modificator chain
        return query.value

    @property
    def defense(self):
        query = Query(self, WhatToQuery.DEFENSE, self.initial_defense)
        self.game.queries(self, query)
        return query.value


class Goblin(Creature):
    def __init__(self, game, attack=1, defense=1):
       super().__init__(game, attack, defense)
       self.game.queries.append(self.handle)

    def handle(self, sender: Creature, query: Query):
        if sender is not self:
            if query.what_to_query == WhatToQuery.DEFENSE:
                query.value += 1
            if isinstance(self, GoblinKing) and query.what_to_query==WhatToQuery.ATTACK:
                query.value +=1

        
class GoblinKing(Goblin):
    def __init__(self, game):
       super().__init__(game, attack=3, defense=3)

class FirstTestSuite(unittest.TestCase):
    def test(self):
        game = Game()
        
        # 1.Spawn first goblin
        goblin1 = Goblin(game)
        game.creatures.append(goblin1)
        self.assertEqual(1, goblin1.attack)
        self.assertEqual(1, goblin1.defense)
        
        # 2. Spawn second goblin
        goblin2 = Goblin(game)
        game.creatures.append(goblin2)
        # Now they defend each other: 1 + 1 bonus = 1/2
        self.assertEqual(1, goblin1.attack)
        self.assertEqual(2, goblin1.defense)
        self.assertEqual(2, goblin2.defense)

        # 3. Add Goblin King (3/3)
        king = GoblinKing(game)
        game.creatures.append(king)
        
        # Ordinary goblins get + 1 to attack from the King
        # and +1 additionally to defense, because the King is also a Goblin.
        # Alltogether ordinary goblin gain: attack (1 + 1 from the King) = 2, defense (1 + 2 from other goblins) = 3
        self.assertEqual(2, goblin1.attack)
        self.assertEqual(3, goblin1.defense)
        
        # The King himself gets bonus to defense from 2 other goblins: 3 + 2 = 5
        # But he will not gain the bonus to attack from himself: stays unchanged - 3
        self.assertEqual(3, king.attack)
        self.assertEqual(5, king.defense)

if __name__ == "__main__":
    unittest.main()