"""
A TokenMachine  is in charge of keeping tokens. 
Each Token  is a reference type with a single numerical value. 
The machine supports adding tokens and, when it does, it returns a memento representing the state of that system at that given time.

You are asked to fill in the gaps and implement the Memento design pattern for this scenario. 
Pay close attention to the situation where a token is fed in as a reference and its value is subsequently changed on that reference 
- you still need to return the correct system snapshot!

"""
from copy import deepcopy

class Token:
    def __init__(self, value=0):
        self.value = value


class Memento(list):
    def __init__(self, tokens):        
        super().__init__([deepcopy(t) for t in tokens])


class TokenMachine:
    def __init__(self):
        self.tokens = []

    def add_token_value(self, value):
        return self.add_token(Token(value))
        

    def add_token(self, token):
        self.tokens.append(token)
        return Memento(self.tokens)

    def revert(self, memento: Memento):
        if memento is not None:
            self.tokens = [deepcopy(t) for t in memento]

if __name__ == "__main__":
    # --- Memento testing ---

    # 1. Machine token init
    machine = TokenMachine()
    print("1. Create machine and add the first token  (value 10)")
    token1 = Token(10)
    memento1 = machine.add_token(token1)

    # 2. Check current state
    print(f"   Current state of the machine: {[t.value for t in machine.tokens]}") # Expect: [10]
    print(f"   State in memento1:      {[t.value for t in memento1]}")      # Expect: [10]

    print("\n--------------------------------------------------")

    # 3. Step to check taht state will persitst if we change token via reference outside of the machine (due to the task conditions):    
    print("2. Change value of the original token token1.value from  10 to 99 outside the machine")
    token1.value = 99

    # Check, what happened
    print(f"   New value of the object token1: {token1.value}")
    print(f"   Current machine state:         {[t.value for t in machine.tokens]}") # Changed becasue of shared reference
    print(f"   Стан у memento1:              {[t.value for t in memento1]}")      # Remains! Due to deepcopy!

    print("\n--------------------------------------------------")

    # 4. Add second token (value = 20, to make task more complicated
    print("3. Add second token  (value = 20) and do memento2")
    memento2 = machine.add_token_value(20)
    print(f"   Current state of the machine: {[t.value for t in machine.tokens]}") # Expect: [99, 20]
    print(f"   State in memento2:      {[t.value for t in memento2]}")      # Expect: [99, 20]

    print("\n--------------------------------------------------")

    # 5. Doing revert to the first snapshot
    print("4. Call revert(memento1) — return to the state, where we had only first tiken with value 10")
    machine.revert(memento1)

    print(f"   Machine state afterrevert: {[t.value for t in machine.tokens]}") # Expect: [10]

    print("\n--------------------------------------------------")

    # 6. Safety check of the archive 
    print("5. Archive safety check")
    machine.tokens[0].value = 555
    print(f"   Changed the contents of the machine after revert to: {[t.value for t in machine.tokens]}") # Expect: [555]
    print(f"   Check, whether memento1 was changed(spoiled):     {[t.value for t in memento1]}")      # Expect: [10] (Stays clean!)
