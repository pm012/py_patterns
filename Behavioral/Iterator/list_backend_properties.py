class Creature:
    _strength = 0
    _agility = 1
    _intelligence = 2



    def __init__(self):
        self.stats = [10, 10, 10]

    @property
    def strength(self):
        return self.stats[Creature._strength]

    @property
    def agility(self):
        return self.stats[Creature._agility]

    @property
    def intelligence(self):
        return self.stats[Creature._intelligence]

    @strength.setter
    def strength(self, value):
        self.stats[Creature._strength] = value

    @agility.setter
    def agility(self, value):
        self.stats[Creature._agility] = value

    @intelligence.setter
    def intelligence(self, value):
        self.stats[Creature._intelligence] = value
    
    
    @property
    def sum_of_stats(self):
        return sum(self.stats)
        #return self.strength + self.intelligence + self.agility

    @property
    def max_stat(self):
        return max(self.stats
        #return max(
            
            #self.strength, self.intelligence, self.agility
        )

    @property
    def average_stat(self):
        return float(sum(self.stats)/len(self.stats))
        #return self.sum_of_stats / 3.0