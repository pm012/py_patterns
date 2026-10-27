class Memento:
    def __init__(self, balance:float):
        self.balance = balance


class BankAccount:
    def __init__(self, balance:float=0.0):
        self.balance = balance

    def deposit(self, amount: float):
        self.balance += amount
        return Memento(self.balance)

    def restore(self, memento: Memento):
        self.balance = memento.balance

    def __str__(self):
        return f"Balance = {self.balance}"

if __name__ == "__main__":
    ba = BankAccount(100)
    m1 = ba.deposit(50)
    m2 = ba.deposit(25)

    print(ba) # 175

    # restore m1

    ba.restore(m1) 

    print(ba) # 150

    # restore m2
    ba.restore(m2)
    print(ba) # 175 again because we don't have memento for the initial state