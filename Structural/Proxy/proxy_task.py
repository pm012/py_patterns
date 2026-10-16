"""
You are given the Person  class and asked to write a ResponsiblePerson  proxy that does the following:

* Allows person to drink unless they are younger than 18 (in that case, return "too young")

* Allows person to drive unless they are younger than 16 (otherwise, "too young")

* In case of driving while drink, returns "dead", regardless of age
"""


class Person:
    def __init__(self, age):
        self.age = age

    def drink(self):
        return 'drinking'

    def drive(self):
        return 'driving'

    def drink_and_drive(self):
        return 'driving while drunk'

class ResponsiblePerson:
    def __init__(self, person: Person):
       self.person = person
       

    @property
    def age(self, value):
        return self.person.age

    @age.setter
    def age(self, value):
        self.perso.age = value

    def drink(self):
        if self.person.age <18:
            return "too young"
        return self.person.drink()
    
        

    def drive(self):
        if self.person.age < 16:
            return "too young"
        return self.person.drive()

    def drink_and_drive(self):
        return 'dead'

if __name__ == "__main__":
    # Test 1: Too young for everything
    child = ResponsiblePerson(Person(10))
    print(child.drink())            # too young
    print(child.drive())            # too young
    print(child.drink_and_drive())  # dead
    
    print("-" * 20)
    
    # Тест 2: Teenager (allowed to drive, not allowed to drink)
    teen = ResponsiblePerson(Person(16))
    print(teen.drink())             # too young
    print(teen.drive())             # driving
    print(teen.drink_and_drive())   # dead
    
    print("-" * 20)
    
    # Test 3: Adult
    adult = ResponsiblePerson(Person(25))
    print(adult.drink())            # drinking
    print(adult.drive())            # driving
    print(adult.drink_and_drive())  # dead
       
        




    





  

