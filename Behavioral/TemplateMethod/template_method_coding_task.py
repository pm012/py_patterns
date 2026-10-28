"""
Imagine a typical collectible card game which has cards representing creatures. 
Each creature has two values: Attack and Health. Creatures can fight each other, dealing their Attack damage, 
thereby reducing their opponent's health.

The class CardGame implements the logic for two creatures fighting one another. 
However, the exact mechanics of how damage is dealt is different:

   * TemporaryCardDamage : In some games (e.g., Magic: the Gathering), unless the creature has been killed, 
   its health returns to the original value at the end of combat.

   * PermanentCardDamage : In other games (e.g., Hearthstone), health damage persists.

You are asked to implement classes TemporaryCardDamageGame  and PermanentCardDamageGame  that would allow us to simulate 
combat between creatures.

Some examples:

    * With temporary damage, creatures 1/2 and 1/3 can never kill one another. With permanent damage, 
    second creature will win after 2 rounds of combat.

    * With either temporary or permanent damage, two 2/2 creatures kill one another.
"""
from abc import ABC, abstractmethod

class Creature:
    def __init__(self, attack, health):
        self.attack = attack
        self.health = health
        self.max_health = health  # Track baseline health for temporary damage resets

class CardGame(ABC):
    def __init__(self, creatures):
        self.creatures = creatures

    # The Template Method: Defines the combat workflow
    def combat(self, c1_index, c2_index):
        c1 = self.creatures[c1_index]
        c2 = self.creatures[c2_index]

        # Attackers deal damage simultaneously
        self.hit(c1, c2)
        self.hit(c2, c1)

        c1_alive = c1.health > 0
        c2_alive = c2.health > 0

        # Post-combat phase: Reset health if it's a temporary damage game and they survived
        self.post_combat_cleanup(c1)
        self.post_combat_cleanup(c2)

        # Determine the winner
        if c1_alive and not c2_alive:
            return c1_index
        elif c2_alive and not c1_alive:
            return c2_index
        else:
            return -1  # Both alive or both dead

    @abstractmethod
    def hit(self, attacker, defender):
        """Primitive operation: Dealt damage mechanics vary by game type."""
        pass

    def post_combat_cleanup(self, creature):
        """Optional hook: Subclasses can override if they need post-combat logic."""
        pass


class TemporaryDamageCardGame(CardGame):
    def hit(self, attacker, defender):
        # Deal damage directly to the current health pool
        defender.health -= attacker.attack

    def post_combat_cleanup(self, creature):
        # Magic: The Gathering style - if the creature survived, heal it back to full
        if creature.health > 0:
            creature.health = creature.max_health


class PermanentDamageCardGame(CardGame):
    def hit(self, attacker, defender):
        # Hearthstone style - damage directly and permanently reduces health pool
        defender.health -= attacker.attack


if __name__ == "__main__":
    # --- Scenario 1: 1/2 vs 1/3 (Temporary vs Permanent) ---
    print("--- Scenario 1: 1/2 vs 1/3 ---")
    
    # Temporary Damage Game (Should result in a draw / -1 indefinitely)
    creatures_temp = [Creature(1, 2), Creature(1, 3)]
    game_temp = TemporaryDamageCardGame(creatures_temp)
    print("Temporary Round 1 Winner index:", game_temp.combat(0, 1)) # -1
    print("Temporary Round 2 Winner index:", game_temp.combat(0, 1)) # -1
    
    # Permanent Damage Game (Creature 2 wins after 2 rounds)
    creatures_perm = [Creature(1, 2), Creature(1, 3)]
    game_perm = PermanentDamageCardGame(creatures_perm)
    print("Permanent Round 1 Winner index:", game_perm.combat(0, 1)) # -1 (C1 has 1hp left, C2 has 2hp left)
    print("Permanent Round 2 Winner index:", game_perm.combat(0, 1)) # 1  (C1 dies, C2 wins with 1hp left)

    # --- Scenario 2: Two 2/2 creatures (Both die in all rule variants) ---
    print("\n--- Scenario 2: 2/2 vs 2/2 ---")
    
    game_temp_clash = TemporaryDamageCardGame([Creature(2, 2), Creature(2, 2)])
    print("Temporary Clash Winner index:", game_temp_clash.combat(0, 1)) # -1 (both dead)

    game_perm_clash = PermanentDamageCardGame([Creature(2, 2), Creature(2, 2)])
    print("Permanent Clash Winner index:", game_perm_clash.combat(0, 1)) # -1 (both dead)

