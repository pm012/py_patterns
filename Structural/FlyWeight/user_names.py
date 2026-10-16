import string
import random

class User:
    def __init__(self, name):
        self.name = name


class User1:
    strings = []
    def __init__(self, name):        

        def add_or_get(s):
            if s in self.strings:
                return self.strings.index(s)
            else:
                self.strings.append(s)
            return len(self.strings) - 1 
        
        self.names = [add_or_get(s) for s in name.split(' ')]

    def __str__(self):
        return ' '.join(self.strings[x] for x in self.names)


def random_string():
    chars = string.ascii_lowercase
    return ''.join([random.choice(chars) for _ in range(8)])

if __name__ == "__main__":
    users = []
    first_names = [random_string() for _ in range(100)]
    last_names = [random_string() for _ in range(100)]

    for first_name in first_names:
        for last_name in last_names:
            users.append(User1(f"{first_name} {last_name}"))

    print(users[0])