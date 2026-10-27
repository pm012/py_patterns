"""
Imagine a game where one or more rats can attack a player. Each individual rat has an initial attack value of 1. 
However, rats attack as a swarm, so each rat's attack value is actually equal to the total number of rats in play.

Given that a rat enters play through the initializer and leaves play (dies) via its __exit__ method, please implement the Game and Rat classes so that, 
at any point in the game, the Attack value of a rat is always consistent.

Here's a sample unit test your code should pass:

def test_three_rats_one_dies(self):
    game = Game()
 
    rat = Rat(game)
    self.assertEqual(1, rat.attack)
 
    rat2 = Rat(game)
    self.assertEqual(2, rat.attack)
    self.assertEqual(2, rat2.attack)
 
    with Rat(game) as rat3:
        self.assertEqual(3, rat.attack)
        self.assertEqual(3, rat2.attack)
        self.assertEqual(3, rat3.attack)
 
    self.assertEqual(2, rat.attack)
    self.assertEqual(2, rat2.attack)
"""
import unittest

class Event(list):
    def __call__(self, *args, **kwds):
        for item in self:
            item(*args, *kwds)


class Game:
    def __init__(self):
        self.rat_counter = 0
        self.on_rat_count_change = Event()

    def add_rat(self):
        self.rat_counter += 1
        self.on_rat_count_change(self.rat_counter)

    def remove_rat(self):
        self.rat_counter -= 1
        self.on_rat_count_change(self.rat_counter)
        


class Rat:
    def __init__(self, game: Game):
        self.game = game
        self.attack = 1

        # Subscrib this rat's update method to the game event
        self.game.on_rat_count_change.append(self.update_attack)
        # Notify Game that the new rat added to play
        self.game.add_rat() 

    def update_attack(self, rat_counter):
        self.attack = rat_counter

    def __enter__(self):
        return self


    def __exit__(self, exc_type, exc, tb):
        # Unsubscribe the rat from the event
        self.game.on_rat_count_change.remove(self.update_attack)
        # Notify the game that this rat has left the game
        self.game.remove_rat()


# Tests
class TestRatSwarm(unittest.TestCase):
    def setUp(self):
        """Runs before every individual test to give us a fresh game instance."""
        self.game = Game()

    def test_single_rat(self):
        """A single rat should have an attack value of 1."""
        with Rat(self.game) as rat1:
            self.assertEqual(rat1.attack, 1)

    def test_swarm_scaling(self):
        """Rats should increase in attack as more join the swarm."""
        with Rat(self.game) as rat1:
            self.assertEqual(rat1.attack, 1)
            
            with Rat(self.game) as rat2:
                # Both rats must scale up to 2
                self.assertEqual(rat1.attack, 2)
                self.assertEqual(rat2.attack, 2)
                
                with Rat(self.game) as rat3:
                    # All three rats must scale up to 3
                    self.assertEqual(rat1.attack, 3)
                    self.assertEqual(rat2.attack, 3)
                    self.assertEqual(rat3.attack, 3)

    def test_rat_death_decreases_swarm_attack(self):
        """Remaining rats should lose attack strength when a rat dies."""
        with Rat(self.game) as rat1:
            with Rat(self.game) as rat2:
                self.assertEqual(rat1.attack, 2)
            
            # rat2 has exited the block (died). rat1 should drop back down to 1.
            self.assertEqual(rat1.attack, 1)

if __name__ == "__main__":
    game = Game()

    # 1. First rat enters
    print("Add 1 rat")
    with Rat(game) as rat1:
        print(f"Rat 1 attack: {rat1.attack}")  # Output: 1

        # 2. Second rat enters
        print("Added second rat")
        with Rat(game) as rat2:
            print(f"Rat 1 attack: {rat1.attack}")  # Output: 2 (Updated via event!)
            print(f"Rat 2 attack: {rat2.attack}")  # Output: 2

        # 3. rat2 dies, triggering the exit logic
        print(f"Rat 1 attack after rat2 dies: {rat1.attack}")  # Output: 1 (Updated via event!)
    # Running unit tests
    print("Running unit tests")
    unittest.main()


