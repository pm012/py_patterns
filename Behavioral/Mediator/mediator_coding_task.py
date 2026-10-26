"""
Our system has any number of instances of Participant  classes. Each Participant has a value integer attribute, initially zero.

A participant can say()  a particular value, which is broadcast to all other participants. 
At this point in time, every other participant is obliged to increase their value  by the value being broadcast.

Example:
Two participants start with values 0 and 0 respectively

Participant 1 broadcasts the value 3. We now have Participant 1 value = 0, Participant 2 value = 3

Participant 2 broadcasts the value 2. We now have Participant 1 value = 2, Participant 2 value = 3
"""


class Mediator:
    
    def __init__(self):        
        self.participants = []
      

    def broadcast(self, sender, value):
        
        for receiver  in self.participants:
             if receiver != sender:
                  receiver.value +=value
        
             


class Participant:
    def __init__(self, mediator:Mediator):
        self.value = 0
        self.mediator = mediator
        self.mediator.participants.append(self)

    def say(self, value):
            self.mediator.broadcast(self, value)

if __name__ == "__main__":
    mediator = Mediator()

p1 = Participant(mediator)
p2 = Participant(mediator)

# Старт: p1.value = 0, p2.value = 0
print(f"Start: p1={p1.value}, p2={p2.value}") 

# Participant 1 broadcasts 3
p1.say(3)
print(f"After p1.say(3): p1={p1.value}, p2={p2.value}") # Awaiting: p1=0, p2=3

# Participant 2 broadcasts 2
p2.say(2)
print(f"After p2.say(2): p1={p1.value}, p2={p2.value}") # Awaiting: p1=2, p2=3

       
