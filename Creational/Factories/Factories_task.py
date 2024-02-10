"""
You are given a class called Person . The person has two attributes: id , and name .

Please implement a  PersonFactory that has a non-static  create_person()  method that takes a person's
name and return a person initialized with this name and an id.

The id of the person should be set as a 0-based index of the object created. So, the first person the factory
makes should have Id=0, second Id=1 and so on.
"""


class Person:
    def __init__(self, id, name):
        self.id = id
        self.name = name

    def __str__(self):
        return f'id: {self.id}, name: {self.name}'


class PersonFactory:
    def __init__(self):
        self.cnt = 0

    def create_person(self, name):
        person = Person(self.cnt, name)
        self.cnt += 1
        return person


if __name__ == '__main__':
    factory = PersonFactory()

    person1 = factory.create_person('Zero')
    print(person1)
    person2 = factory.create_person('One')
    print(person2)
