class Event(list):
    def __call__(self, *args, **kwds):
        for item in self:
            item(*args, **kwds)

class PropertyObservable:
    def __init__(self):
        self.property_changed = Event()

class Person(PropertyObservable):
    def __init__(self, age=0):
        super().__init__()
        self._age = age

    @property
    def can_vote(self):
        return self._age >= 18    
   
    @property
    def age(self):
        return self._age

    @age.setter
    def age(self, value):
        if self._age == value:
            return
        
        old_can_vote = self.can_vote
        self._age = value
        self.property_changed('age', value)
        # self.property_changed('can_vote', value) incorrect way of implementation the event vote_change
        if old_can_vote != self.can_vote:
            self.property_changed('can_vote', self.can_vote)

def person_changed(name, value):
    if name == 'can_vote':
        print(f'Voting ability changed to {value}')


if __name__ == "__main__":
    p = Person()
    p.property_changed.append(person_changed)

    
    for age in range(16, 21):
        print(f'Changing age to {age}')
        p.age = age



    