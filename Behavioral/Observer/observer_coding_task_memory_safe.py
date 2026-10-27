import unittest
import weakref

class Event:
    def __init__(self):
        # We use a list to store our weak references
        self._listeners = []

    def append(self, callback):
        # weakref.WeakMethod handles bound methods safely
        self._listeners.append(weakref.WeakMethod(callback))

    def remove(self, callback):
        # To remove, find the WeakMethod that points to the same underlying callback
        for ref in list(self._listeners):
            if ref() == callback or ref == callback:
                self._listeners.remove(ref)
                break

    def __call__(self, *args, **kwds):
        # Iterate over a copy of the list to safely modify it during execution if needed
        for ref in list(self._listeners):
            callback = ref()  # Resolving the weak reference
            if callback is not None:
                callback(*args, **kwds)
            else:
                # Clean up "dead" references automatically when the event is triggered
                self._listeners.remove(ref)


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

        # Subscribing this rat's update method to the game event safely
        self.game.on_rat_count_change.append(self.update_attack)
        self.game.add_rat() 

    def update_attack(self, rat_counter):
        self.attack = rat_counter

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc, tb):
        # Explicit clean-up is still good practice
        self.game.on_rat_count_change.remove(self.update_attack)
        self.game.remove_rat()


# --- Unit Tests ---
class TestRatSwarm(unittest.TestCase):
    def setUp(self):
        self.game = Game()

    def test_single_rat(self):
        with Rat(self.game) as rat1:
            self.assertEqual(rat1.attack, 1)

    def test_swarm_scaling(self):
        with Rat(self.game) as rat1:
            self.assertEqual(rat1.attack, 1)
            with Rat(self.game) as rat2:
                self.assertEqual(rat1.attack, 2)
                self.assertEqual(rat2.attack, 2)
                with Rat(self.game) as rat3:
                    self.assertEqual(rat1.attack, 3)
                    self.assertEqual(rat2.attack, 3)
                    self.assertEqual(rat3.attack, 3)

    def test_rat_death_decreases_swarm_attack(self):
        with Rat(self.game) as rat1:
            with Rat(self.game) as rat2:
                self.assertEqual(rat1.attack, 2)
            self.assertEqual(rat1.attack, 1)

    def test_memory_leak_safety(self):
        """Verify that a Rat can be garbage collected even if not explicitly unsubscribed."""
        import gc
        
        # Create a rat locally outside of a 'with' context manager
        leaky_rat = Rat(self.game)
        self.assertEqual(self.game.rat_counter, 1)
        
        # Completely delete all our local strong references to this rat
        del leaky_rat
        gc.collect()  # Force Python's garbage collector to run
        
        # Triggering the event will now cleanly purge the dead weakref from the list
        self.game.on_rat_count_change(100)
        
        # The internal list should be completely empty now
        self.assertEqual(len(self.game.on_rat_count_change._listeners), 0)


if __name__ == "__main__":
    game = Game()

    print("--- Running Demo Simulation ---")
    print("Add 1 rat")
    with Rat(game) as rat1:
        print(f"Rat 1 attack: {rat1.attack}")

        print("Added second rat")
        with Rat(game) as rat2:
            print(f"Rat 1 attack: {rat1.attack}")
            print(f"Rat 2 attack: {rat2.attack}")

        print(f"Rat 1 attack after rat2 dies: {rat1.attack}")
    
    print("\n--- Running Unit Tests ---")
    # Clean up sys.argv so unittest doesn't get confused by extra execution parameters
    import sys
    unittest.main(argv=[sys.argv[0]], exit=False)
