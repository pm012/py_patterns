from abc import abstractmethod


class Person:
    def __init__(self):
        self.name = None
        self.position = None
        self.date_of_birth = None

    def __str__(self):
        return f'{self.name} born on {self.date_of_birth} ' + \
            f'works as {self.position}'

    @staticmethod
    def new():
        return PersonJobBuilder()


class PersonBuilder:
    def __init__(self):
        self.person = Person()

    def build(self):
        return self.person


class PersonInfoBuilder(PersonBuilder):
    def called(self, name):
        self.person.name = name
        return self


class PersonJobBuilder(PersonInfoBuilder):
    def works_as_a(self, position):
        self.person.position = position
        return self


class PersonDateBuilder(PersonJobBuilder):
    def born(self, date_of_birth):
        self.person.date_of_birth = date_of_birth
        return self


pb = PersonDateBuilder()
me = pb \
    .called('Serhii') \
    .works_as_a('QA') \
    .born('1/1/1908') \
    .build()

print(me)

pb2 = Person.new().called('John').works_as_a('Worker').build()
print(pb2)
