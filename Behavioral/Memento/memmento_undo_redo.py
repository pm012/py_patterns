class Memento:
    def __init__(self, balance:float):
        self.balance = balance


class BankAccount:
    def __init__(self, balance:float=0.0):
        self.balance = balance
        self.changes = [Memento(self.balance)]
        self.current = 0 # index of changes list

    def deposit(self, amount: float):
        self.balance += amount
        m =  Memento(self.balance)
        self.changes.append(m)
        self.current += 1
        return m

    def restore(self, memento: Memento):
        if memento:
            self.balance = memento.balance
            self.changes.append(memento)
            self.current = len(self.changes)-1

    def undo(self):
        if self.current > 0:
            self.current -= 1
            m = self.changes[self.current]
            self.balance = m.balance
            return m
        return None

    def redo(self):
        if self.current + 1 < len(self.changes):
            self.current += 1
            m = self.changes[self.current]
            self.balance = m.balance
            return m
        return None

    def __str__(self):
        return f"Balance = {self.balance}"

if __name__ == "__main__":
    ba = BankAccount(100)
    m1 = ba.deposit(50)
    m2 = ba.deposit(25)

    print(ba) # 175

    # restore m1

    ba.undo()

    print(f'Undo 1: {ba}') # 150

    # restore m2
    ba.undo()
    print(f'Undo 2: {ba}') # 100 

    ba.redo()   
    print(f'Redo 1: {ba}') # 150