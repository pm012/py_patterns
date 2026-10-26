class Person:
    def __init__(self, name: str):
        self.name = name
        self.chat_log = []
        self.room: ChatRoom = None

    def receive(self, sender: Person, message:str):
        s = f'{sender}: {message}'
        print(f'[{self.name}\'s chat session] {s}')
        self.chat_log.append(s)

    def private_message(self, who:Person, message:Person):
        self.room.mesage(self.name, who, message)

    def say(self, message:str):
        self.room.broadcast(self.name, message)

class ChatRoom:
    def __init__(self):
        self.people = []

    def join(self, person:Person):
        join_msg = f'{person.name} joins the chat'
        self.broadcast('room ', join_msg)
        person.room = self
        self.people.append(person)

    def broadcast(self, source: Person, message: str):
        for p in self.people:
            if p.name != source:
                p.receive(source, message)

    def mesage(self, source, destination, message):
        for p in self.people:
            if p.name == destination:
                p.receive(source, message)

if __name__ == "__main__":
    room = ChatRoom()

    john = Person("John")
    jane = Person("Jane")

    room.join(john)
    room.join(jane)

    john.say('hi room!')
    jane.say('Oh, hey John')

    simon = Person('Simon')

    room.join(simon)

    simon.say('Hi everyone')

    jane.private_message("Simon", 'glad you could join us')


        